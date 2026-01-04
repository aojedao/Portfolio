#!/usr/bin/env python3
"""Simulate the exact JavaScript parsing logic"""

def parse_csv_flat(csv_text):
    """Simulate parseCSVFlat"""
    if not csv_text:
        return []
    values = (csv_text
              .replace('\r\n', ',')
              .replace('\n', ',')
              .split(','))
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
    """Simulate parseCSVColumns"""
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

def extract_data(raw_text, col_idx):
    """Simulate the JavaScript extraction logic"""
    # Try column-based parsing first
    cols = parse_csv_columns(raw_text)
    data = []
    
    if cols and len(cols[0]) > col_idx:
        data = [row[col_idx] for row in cols if col_idx < len(row)]
    
    # Fall back to flat parsing
    if not data:
        data = parse_csv_flat(raw_text)
    
    return data

# Test 1: Servos Cartesian (columns)
print("Test 1: Servos Cartesian Path")
cartesian = """X_Position,Y_Position
0.101629490116335,0.00255476560883914
0.101286204249937,0.00509549210119244"""

x_data = extract_data(cartesian, 0)
y_data = extract_data(cartesian, 1)
print(f"  X (column 0): {len(x_data)} values → {x_data[:2]}")
print(f"  Y (column 1): {len(y_data)} values → {y_data[:2]}")
assert len(x_data) == 2, f"Expected 2 X values, got {len(x_data)}"
assert len(y_data) == 2, f"Expected 2 Y values, got {len(y_data)}"
print("  ✓ PASS")

# Test 2: Servos Joint Dynamics (multi-column)
print("\nTest 2: Servos Joint Dynamics")
joint = """Time,Theta1,Theta2,Vel1,Vel2
0,8.28318521742886,-3.68318526590152,-31.3109199847877,-0.0117661968885978
0.100401337792642,5.13952696343779,-3.68436660780986,-31.3109199847877,-0.0235918179186145"""

time_data = extract_data(joint, 0)
theta1_data = extract_data(joint, 1)
theta2_data = extract_data(joint, 2)
print(f"  Time (column 0): {len(time_data)} values")
print(f"  Theta1 (column 1): {len(theta1_data)} values")
print(f"  Theta2 (column 2): {len(theta2_data)} values")
assert len(time_data) == 2, f"Expected 2 time values"
assert len(theta1_data) == 2, f"Expected 2 theta1 values"
assert len(theta2_data) == 2, f"Expected 2 theta2 values"
print("  ✓ PASS")

# Test 3: Ebarisbot flat CSV
print("\nTest 3: Ebarisbot Torque Profile (Flat)")
flat = "0.367,0.367,0.367,0.01778,0.01778,0.349,0.349"

t_data = extract_data(flat, 0)  # Should use flat parsing
print(f"  Time data (flat): {len(t_data)} values → {t_data[:3]}")
assert len(t_data) == 7, f"Expected 7 values, got {len(t_data)}"
print("  ✓ PASS")

print("\n✓ All parsing logic verified!")
