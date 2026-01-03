import pandas as pd
import matplotlib.pyplot as plt
import os

# Define paths
base_dir = r"f:/MESGRO/temp_servos_import"
output_dir = r"f:/MESGRO/assets/images/projects/servos"
cartesian_file = os.path.join(base_dir, "robot_cartesian_path.csv")
dynamics_file = os.path.join(base_dir, "robot_joint_dynamics.csv")

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Plot Cartesian Path
try:
    df_cart = pd.read_csv(cartesian_file)
    plt.figure(figsize=(8, 6))
    plt.plot(df_cart['X_Position'], df_cart['Y_Position'], label='End Effector Path')
    plt.title('Robot Cartesian Path (X vs Y)')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "cartesian_path.png"))
    plt.close()
    print("Generated cartesian_path.png")
except Exception as e:
    print(f"Error plotting cartesian path: {e}")

# Plot Joint Dynamics
try:
    df_dyn = pd.read_csv(dynamics_file)
    # df_dyn columns: Time, Theta1, Theta2, Vel1, Vel2
    
    # Theta 1
    plt.figure(figsize=(8, 4))
    plt.plot(df_dyn['Time'], df_dyn['Theta1'], color='tab:blue')
    plt.title('Joint 1 Position (Theta1)')
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "theta1_dynamics.png"))
    plt.close()

    # Theta 2
    plt.figure(figsize=(8, 4))
    plt.plot(df_dyn['Time'], df_dyn['Theta2'], color='tab:orange')
    plt.title('Joint 2 Position (Theta2)')
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "theta2_dynamics.png"))
    plt.close()

    # Velocity 1
    plt.figure(figsize=(8, 4))
    plt.plot(df_dyn['Time'], df_dyn['Vel1'], color='tab:green')
    plt.title('Joint 1 Velocity (Vel1)')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (rad/s)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vel1_dynamics.png"))
    plt.close()

    # Velocity 2
    plt.figure(figsize=(8, 4))
    plt.plot(df_dyn['Time'], df_dyn['Vel2'], color='tab:red')
    plt.title('Joint 2 Velocity (Vel2)')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (rad/s)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vel2_dynamics.png"))
    plt.close()
    
    print("Generated dynamics plots")

except Exception as e:
    print(f"Error plotting dynamics: {e}")
