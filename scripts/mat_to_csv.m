% MAT_TO_CSV_CONVERTER
% This script loads a .mat file and saves all its numeric matrices and tables as CSV files.

% --- CONFIGURATION ---
% Replace 'YourFile.mat' with your actual file name
inputMatFile = 'Tornillos_Data.mat'; 
outputFolder = 'csv_exports';
% ---------------------

% Create output folder if it doesn't exist
if ~exist(outputFolder, 'dir')
    mkdir(outputFolder);
end

% Check if file exists
if ~isfile(inputMatFile)
    fprintf('Error: The file "%s" was not found in the current folder.\n', inputMatFile);
    fprintf('Please ensure your .mat file is in the same folder as this script, or provide the full path.\n');
    return;
end

% Load the .mat file data
fprintf('Loading %s...\n', inputMatFile);
dataStruct = load(inputMatFile);
variableNames = fieldnames(dataStruct);

count = 0;

% Iterate through every variable in the .mat file
for i = 1:length(variableNames)
    varName = variableNames{i};
    val = dataStruct.(varName);
    
    % Prepare the output filename
    outputFileName = fullfile(outputFolder, [varName '.csv']);
    
    % Check data type
    if istable(val) || istimetable(val)
        writetable(val, outputFileName);
        fprintf('✅ Saved TABLE "%s" to %s\n', varName, outputFileName);
        count = count + 1;
        
    elseif isnumeric(val) && ~isscalar(val)
        writematrix(val, outputFileName);
        fprintf('✅ Saved MATRIX "%s" to %s\n', varName, outputFileName);
        count = count + 1;
        
    elseif isscalar(val) && isnumeric(val)
        fprintf('ℹ️  Skipping SCALAR "%s" (single number)\n', varName);
        
    else
        fprintf('⚠️  Skipping "%s" (Type: %s is not automatically supported for CSV)\n', varName, class(val));
    end
end

fprintf('\nDone! Exported %d files to the "%s" folder.\n', count, outputFolder);
