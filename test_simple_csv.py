#!/usr/bin/env python3
"""Test parsing with simple CSV files"""

def parse_csv_flat(csv_text):
    """Parse flat CSV"""
    if not csv_text:
        return []
    values = csv_text.replace('\r\n', ',').replace('\n', ',').split(',')
    result = []
    for v in values:
        v = v.strip()
        if v and not (v[0].isalpha()):  # Skip text values
            try:
                result.append(float(v))
            except:
                pass
    return result

def parse_csv_columns(csv_text):
    """Parse columnar CSV"""
    if not csv_text:
        return []
    lines = [l.strip() for l in csv_text.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return []
    
    # Check if first line is header
    first_parts = lines[0].split(',')
    is_header = any(p.strip() for p in first_parts if not is_numeric(p))
    
    data_lines = lines[1:] if is_header else lines
    result = []
    for line in data_lines:
        row = []
        for v in line.split(','):
            v = v.strip()
            if is_numeric(v):
                row.append(float(v))
            else:
                row.append(None)
        result.append(row)
    return result

def is_numeric(s):
    try:
        float(s)
        return True
    except:
        return False

# Test 1: Ebarisbot flat CSV
print("Test 1: Ebarisbot flat CSV")
ebarisbot_t = "0,0.5,1,1.5,2,2.5,3,3.5,4"
ebarisbot_torque = "0.367,0.367,0.367,0.0178,0.0178,0.349,0.349,0.349,0.3"

t_data = parse_csv_flat(ebarisbot_t)
torque_data = parse_csv_flat(ebarisbot_torque)

print(f"  Time: {t_data}")
print(f"  Torque: {torque_data}")
print(f"  Lengths match: {len(t_data) == len(torque_data)}")
if len(t_data) == len(torque_data) and len(t_data) > 0:
    print(f"  ✓ PASS")
else:
    print(f"  ✗ FAIL")

# Test 2: Servos Cartesian
print("\nTest 2: Servos Cartesian (Columnar CSV)")
cartesian_csv = """X_Position,Y_Position
0.0,0.0
0.1,0.05
0.2,0.08
0.3,0.1"""

cols = parse_csv_columns(cartesian_csv)
if cols:
    x_data = [row[0] for row in cols if row[0] is not None]
    y_data = [row[1] for row in cols if row[1] is not None]
    print(f"  X data (column 0): {x_data}")
    print(f"  Y data (column 1): {y_data}")
    if len(x_data) == len(y_data) and len(x_data) > 0:
        print(f"  ✓ PASS")
    else:
        print(f"  ✗ FAIL")
else:
    print(f"  ✗ FAIL: No data parsed")

# Test 3: Servos Joint
print("\nTest 3: Servos Joint (Multi-column CSV)")
joint_csv = """Time,Theta1,Theta2,Vel1,Vel2
0,1.57,-1.57,0,0
0.1,1.5,-1.65,0.7,-0.8
0.2,1.4,-1.73,0.7,-0.8"""

cols = parse_csv_columns(joint_csv)
if cols:
    time_data = [row[0] for row in cols if row[0] is not None]
    theta1_data = [row[1] for row in cols if row[1] is not None]
    theta2_data = [row[2] for row in cols if row[2] is not None]
    print(f"  Time (column 0): {time_data}")
    print(f"  Theta1 (column 1): {theta1_data}")
    print(f"  Theta2 (column 2): {theta2_data}")
    if len(time_data) == len(theta1_data) == len(theta2_data) and len(time_data) > 0:
        print(f"  ✓ PASS")
    else:
        print(f"  ✗ FAIL")
else:
    print(f"  ✗ FAIL: No data parsed")

print("\nAll tests completed!")
