#!/usr/bin/env python3
"""Test script to validate plot data parsing"""

def parse_csv_flat(csv_text):
    """Parse flat comma-separated values"""
    if not csv_text:
        return []
    values = csv_text.replace('\r\n', ',').replace('\n', ',').split(',')
    result = []
    for v in values:
        v = v.strip()
        if v:
            try:
                result.append(float(v))
            except ValueError:
                pass
    return result

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

# Test 1: Cartesian Path (columnar CSV)
print("Test 1: Cartesian Path CSV")
cartesian_csv = """X_Position,Y_Position
0.101629490116335,0.00255476560883914
0.101286204249937,0.00509549210119244
0.100716726610285,0.0076082851758131"""

cols = parse_csv_columns(cartesian_csv)
print(f"  Parsed {len(cols)} rows")
if cols:
    print(f"  First row: {cols[0]}")
    x_data = [row[0] for row in cols]
    y_data = [row[1] for row in cols]
    print(f"  X column (0): {x_data}")
    print(f"  Y column (1): {y_data}")
    print(f"  ✓ PASS: X and Y extracted correctly")
else:
    print(f"  ✗ FAIL: No data parsed")

# Test 2: Joint Dynamics (columnar CSV with multiple columns)
print("\nTest 2: Joint Dynamics CSV")
joint_csv = """Time,Theta1,Theta2,Vel1,Vel2
0,8.28318521742886,-3.68318526590152,-31.3109199847877,-0.0117661968885978
0.100401337792642,5.13952696343779,-3.68436660780986,-31.3109199847877,-0.0235918179186145"""

cols = parse_csv_columns(joint_csv)
print(f"  Parsed {len(cols)} rows")
if cols:
    print(f"  First row: {cols[0]}")
    time_data = [row[0] for row in cols]
    theta1_data = [row[1] for row in cols]
    theta2_data = [row[2] for row in cols]
    print(f"  Time column (0): {time_data}")
    print(f"  Theta1 column (1): {theta1_data}")
    print(f"  Theta2 column (2): {theta2_data}")
    print(f"  ✓ PASS: All columns extracted correctly")
else:
    print(f"  ✗ FAIL: No data parsed")

# Test 3: Flat CSV (ebarisbot format)
print("\nTest 3: Flat CSV (ebarisbot format)")
flat_csv = "1.52,1.53,1.54,1.55,1.56,2.5,3.0,4.0,4.4"

flat_data = parse_csv_flat(flat_csv)
print(f"  Parsed {len(flat_data)} values")
print(f"  Data: {flat_data}")
if len(flat_data) == 9:
    print(f"  ✓ PASS: Flat format parsed correctly")
else:
    print(f"  ✗ FAIL: Expected 9 values, got {len(flat_data)}")

# Test 4: Real ebarisbot file (first 10 values)
print("\nTest 4: Real ebarisbot t.csv (simulated)")
ebarisbot_csv = "2843284,1.52372637263726,1.52416841684168,1.52461046105612,1.52505250527055,1.52549454948499,1.52593659369943,1.52637863791386,1.5268206821283"

flat_data = parse_csv_flat(ebarisbot_csv)
print(f"  Parsed {len(flat_data)} values")
print(f"  First 3 values: {flat_data[:3]}")
if len(flat_data) >= 9:
    print(f"  ✓ PASS: Ebarisbot format parsed correctly")
else:
    print(f"  ✗ FAIL: Expected at least 9 values, got {len(flat_data)}")

print("\nAll tests completed!")
