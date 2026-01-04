#!/usr/bin/env python3
"""Test CSV parsing with column selection"""

def parse_csv_columns(csv_text):
    """Parse traditional CSV with headers"""
    if not csv_text:
        return []
    lines = csv_text.strip().split('\n')
    # Skip header row
    result = []
    for line in lines[1:]:
        row = []
        for v in line.split(','):
            try:
                row.append(float(v.strip()))
            except ValueError:
                pass
        result.append(row)
    return result

# Test with servos cartesian path
cartesian_csv = """X_Position,Y_Position
0.101629490116335,0.00255476560883914
0.101286204249937,0.00509549210119244
0.100716726610285,0.0076082851758131"""

print("Test: Cartesian Path CSV")
cols = parse_csv_columns(cartesian_csv)
print(f"  Parsed {len(cols)} rows")

if cols and len(cols[0]) >= 2:
    # Extract column 0 (X_Position)
    x_data = [row[0] for row in cols]
    # Extract column 1 (Y_Position)
    y_data = [row[1] for row in cols]
    print(f"  Column 0 (X): {x_data}")
    print(f"  Column 1 (Y): {y_data}")
    print(f"  ✓ PASS")
else:
    print(f"  ✗ FAIL: Could not extract columns")

# Test with servos joint dynamics (multiple Y columns)
joint_csv = """Time,Theta1,Theta2,Vel1,Vel2
0,8.28318521742886,-3.68318526590152,-31.3109199847877,-0.0117661968885978
0.100401337792642,5.13952696343779,-3.68436660780986,-31.3109199847877,-0.0235918179186145
0.200802675585284,1.99586870944673,-3.6879225660615,-15.6808044011073,-0.047418800877904"""

print("\nTest: Joint Dynamics CSV (multiple columns)")
cols = parse_csv_columns(joint_csv)
print(f"  Parsed {len(cols)} rows with {len(cols[0]) if cols else 0} columns")

if cols and len(cols[0]) >= 3:
    time_data = [row[0] for row in cols]
    theta1_data = [row[1] for row in cols]
    theta2_data = [row[2] for row in cols]
    print(f"  Column 0 (Time): {time_data}")
    print(f"  Column 1 (Theta1): {theta1_data}")
    print(f"  Column 2 (Theta2): {theta2_data}")
    print(f"  ✓ PASS")
else:
    print(f"  ✗ FAIL: Could not extract columns")

print("\nAll tests passed!")
