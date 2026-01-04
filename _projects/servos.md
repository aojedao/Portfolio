---
layout: project
title: "2-DOF Robotic Arm Parametric Trajectory"
date: 2026-01-03
featured_image: "/assets/images/projects/servos/mechanics_explorer.gif"
description: "Implementation of inverse kinematics and trajectory planning for a 2-DOF planar robot arm to trace a complex geometric path, simulated in MATLAB/Simscape."
category: "Robotics"
tags: [MATLAB, Simscape, Inverse Kinematics, Robotics, Control Systems]
plots_title: "Data Visualization"
plots:
  - title: "Cartesian Path (X vs Y)"
    x_file: "/assets/data/servos/robot_cartesian_simple.csv"
    x_column: 0
    y_files:
      - file: "/assets/data/servos/robot_cartesian_simple.csv"
        column: 1
        label: "End Effector Path"
    x_label: "X Position (m)"
    y_label: "Y Position (m)"
  - title: "Joint Angles Over Time"
    x_file: "/assets/data/servos/robot_joint_simple.csv"
    x_column: 0
    y_files:
      - file: "/assets/data/servos/robot_joint_simple.csv"
        column: 1
        label: "Joint 1 Angle (Theta 1)"
      - file: "/assets/data/servos/robot_joint_simple.csv"
        column: 2
        label: "Joint 2 Angle (Theta 2)"
    x_label: "Time (s)"
    y_label: "Angle (rad)"
custom_plot: "universal-plot-handler.html"
models:
  - file: "/assets/models/servos/arm.gltf"
    description: "3D Model of the 2-DOF Arm"
gallery:
  - file: "/assets/images/projects/servos/trajectory_animation.gif"
    description: "Trajectory evolution animation"

  - file: "/assets/images/projects/servos/mechanics_explorer.gif"
    description: "Simscape Multibody simulation of the arm tracing the target path"
  - file: "/assets/images/projects/servos/cartesian_path.png"
    description: "Generated Cartesian path (Stylized Clover)"
  - file: "/assets/images/projects/servos/DataInspector.png"
    description: "Simulink Data Inspector results"
  - file: "/assets/images/projects/servos/theta1_dynamics.png"
    description: "Joint 1 Angle (Theta 1) over time"
  - file: "/assets/images/projects/servos/theta2_dynamics.png"
    description: "Joint 2 Angle (Theta 2) over time"
  - file: "/assets/images/projects/servos/vel1_dynamics.png"
    description: "Joint 1 Velocity profile"
  - file: "/assets/images/projects/servos/vel2_dynamics.png"
    description: "Joint 2 Velocity profile"
  - file: "/assets/images/projects/servos/LogicAnalyzer.png"
    description: "Control Logic Analysis"
---

## Project Overview

This project involves the kinematic analysis and simulation of a 2-Degree-of-Freedom (2-DOF) planar robotic manipulator. The primary objective was to design a control system capable of guiding the robot's end-effector to trace a stylized clover shape defined by parametric equations.

The project demonstrates the application of **Inverse Kinematics (IK)** to map Cartesian task-space coordinates to the robot's joint-space configuration, and uses **MATLAB Simscape Multibody** for high-fidelity physical simulation.

## Mathematical Formulation

### Path Generation
The target trajectory is a stylized three-leaf clover, mathematically defined in polar coordinates by the equation:

$$ \rho = \frac{4+\cos(3(\theta -\gamma))}{10} $$

Where $\rho$ is the radial distance and $\theta$ is the angle. This path is discretized and converted into Cartesian coordinates $(x, y)$ to serve as the reference setpoints for the robot.

### Inverse Kinematics
To control the arm, we solved the inverse kinematics problem using geometric methods. For a given target position $(x, y)$, the required joint angles $q_1$ and $q_2$ were calculated. We considered both "Elbow Up" and "Elbow Down" configurations.

Using the Law of Cosines, the intermediate angle $\alpha$ is determined by:

$$ \alpha = \arccos\left(\frac{l_1^2 + r^2 - l_2^2}{2 l_1 r}\right) $$

where $l_1$ and $l_2$ are the link lengths ($l_1 = 0.22m, l_2 = 0.17m$) and $r$ is the distance from the base to the target.

## Simulation & Results

The mathematical model was implemented in MATLAB to generate the joint trajectories. These trajectories were then fed into a **Simscape Multibody** model of the robot.

The simulation results confirmed the accuracy of the kinematic model. The plots (see right panel) show the resulting joint dynamics and the successful tracking of the Cartesian path.


### Resources
- [Download Full Report (PDF)](/assets/schematics/servos/report.pdf)
- [View HTML Report](/assets/schematics/servos/report.html)
- [Download 3D Model (GLTF)](/assets/models/servos/arm.gltf)
