---
layout: project
title: "Autonomous Navigation & SLAM"
subtitle: "ROS Kinetic Lab: Mapping and Localization with Turtlebot"
description: "Experimental implementation of Simultaneous Localization and Mapping (SLAM) and autonomous navigation using AMCL and move_base stack on ROS Kinetic."
date: 2022-02-03
categories: [Robotics, ROS, SLAM, Autonomous Navigation]
difficulty: Intermediate
featured_image: "/assets/images/projects/practica/demo.gif"
github_url: ""
demo_url: ""
tags: [ROS Kinetic, Turtlebot, SLAM, Gmapping, AMCL, Python, C++]

code_files:
  - name: "SLAM & Navigation Commands"
    file: "ros_commands.sh"
    language: "bash"
    content: |
      # --- PHASE 1: SLAM (Mapping) ---
      
      # 1. Launch the Simulation (Gazebo)
      roslaunch turtlebot_gazebo turtlebot_world.launch
      
      # 2. Launch Gmapping (SLAM)
      roslaunch turtlebot_gazebo gmapping_demo.launch
      
      # 3. Launch Teleoperation (to drive the robot)
      roslaunch turtlebot_teleop keyboard_teleop.launch
      
      # 4. Save the Map (after driving around)
      rosrun map_server map_saver -f /tmp/my_map
      
      
      # --- PHASE 2: Autonomous Navigation (AMCL) ---
      
      # 1. Launch the Simulation (if not already running)
      roslaunch turtlebot_gazebo turtlebot_world.launch
      
      # 2. Launch AMCL (Localization & Path Planning)
      # Note: Point to the map file you saved earlier
      roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/tmp/my_map.yaml
      
      # 3. Launch Rviz (Visualization)
      roslaunch turtlebot_rviz_launchers view_navigation.launch
      
      # INSTRUCTIONS:
      # In Rviz, use "2D Pose Estimate" to set initial location.
      # Use "2D Nav Goal" to send the robot to a destination.

schematics:
  - file: "/assets/schematics/practica/guia_navegacion.pdf"
    description: "Autonomous Navigation Guide (AMCL - ROS Kinetic)"
  - file: "/assets/schematics/practica/guia_slam.pdf"
    description: "SLAM Implementation Guide (ROS Kinetic)"

gallery:
  - file: "/assets/images/projects/practica/demo.gif"
    description: "Simulation of autonomous navigation in Rviz vs Gazebo"
  - file: "/assets/images/projects/practica/rviz_map.png"
    description: "Generated 2D Occupancy Grid Map in Rviz"
  - file: "/assets/images/projects/practica/terminals.png"
    description: "ROS Node initialization and topic monitoring"
  - file: "/assets/images/projects/practica/process.png"
    description: "Navigation stack configuration process"

---

## Overview

This project focuses on the practical implementation of autonomous navigation capabilities for mobile robots using the **Robot Operating System (ROS)**, specifically the **Kinetic Kame** distribution. The primary objective is to enable a robot (Turtlebot platform) to map an unknown environment and subsequently navigate within it autonomously while avoiding dynamic and static obstacles.

## Key Technologies

- **ROS Kinetic**: Middleware framework for robot software development.
- **SLAM (Gmapping)**: Implementation of FastSLAM algorithm for creating 2D occupancy grid maps from laser scan data.
- **AMCL**: Adaptive Monte Carlo Localization for probabilistic estimation of the robot's pose within a known map.
- **move_base**: The ROS navigation stack package that links the global and local planners to drive the robot base.

## Methodology

### 1. Mapping (SLAM)
The first phase involves creating a map of the environment. Using the `gmapping` package, the robot navigates the environment (teleoperated) while processing data from its LIDAR/depth sensor and odometry.
*   **Sensor Fusion**: Combining wheel odometry drift with laser scan matching.
*   **Grid Mapping**: Generating a static map where black pixels represent obstacles, white pixels are free space, and gray areas are unknown.

### 2. Localization (AMCL)
Once the map is generated, the **Adaptive Monte Carlo Localization (AMCL)** algorithm is used.
*   **Particle Filter**: Uses a cloud of particles to represent possible robot poses.
*   **Resampling**: As the robot moves and senses the environment, particles that match sensor readings converge to the true robot location.

### 3. Path Planning
The `move_base` node handles the actual navigation:
*   **Global Planner**: Calculates the optimal path from start to goal (e.g., Dijkstra or A*).
*   **Local Planner**: Generates velocity commands (`cmd_vel`) to follow the global path while avoiding dynamic obstacles (Dynamic Window Approach).

## Implementation Results

The project successfully demonstrated the complete navigation loop:
1.  **Map Generation**: A high-fidelity map of the lab environment was created using Gmapping.
2.  **Autonomous Routing**: The robot successfully planned and executed paths between arbitrary points in the map.
3.  **Obstacle Avoidance**: The system dynamically re-planned paths when encountering unmapped obstacles.

## Resources

The full implementation guides are available as PDF documents in the schematics section above, covering the step-by-step commands and configuration parameters used during the lab practice.
