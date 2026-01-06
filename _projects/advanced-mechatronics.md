---
layout: project
title: "Advanced Mechatronics - Autonomous Container Handling Swarm System"
description: "Advanced Mechatronics course project: Autonomous Container Handling Swarm System (ACHSS). Multi-phase project featuring robotic swarm design with Phase 1 (Pandebono), Phase 2 (Mate - Propeller-Based Robot), and Phase 3 (Integrated System). Includes 3D models, mechanical design, and swarm robotics implementation."
date: 2025-05-07
categories: [Mechatronics, Swarm Robotics, Autonomous Systems, 3D Design, CAD, Advanced Engineering]
featured_image: "/assets/images/projects/advancedmechatronics/project.jpg"
github_url: "#"
demo_url: "#"

# 3D Models - Components and Assembly
models:
  - file: "/assets/models/advancedmechatronics/CompleteSystem.gltf"
    bin_file: "/assets/models/advancedmechatronics/CompleteSystem.bin"
    description: "Phase 3 - Complete Autonomous Container Handling Swarm System (ACHSS) with all integrated components and subsystems"
  - file: "/assets/models/advancedmechatronics/Pandebono.gltf"
    bin_file: "/assets/models/advancedmechatronics/Pandebono.bin"
    description: "Phase 1 (Mini Project 1) - Pandebono: Inaugural propeller-based robotic platform design"
  - file: "/assets/models/advancedmechatronics/Mate.gltf"
    bin_file: "/assets/models/advancedmechatronics/Mate.bin"
    description: "Phase 2 (Mini Project 2) - Mate: Refined propeller-based two-wheel autonomous robot with enhanced design"

# Gallery - Images, Videos, and Documentation
gallery:
  - file: "/assets/images/projects/advancedmechatronics/complete-system.png"
    description: "Complete System Assembly - Phase 3 integrated design with all subsystems"
  - file: "/assets/images/projects/advancedmechatronics/robot-demo.jpg"
    description: "Operational robot prototype during testing and validation"
  - file: "/assets/images/projects/advancedmechatronics/speed-controller-test.gif"
    description: "Speed controller demonstration from test results - shows motor control dynamics and response"
  - file: "/assets/images/projects/advancedmechatronics/position-control.gif"
    description: "Position control feedback - visualization of autonomous navigation"

# Interactive Data Visualizations
visualizations:
  - file: "/assets/images/projects/advancedmechatronics/acceleration-plot.html"
    description: "Interactive Acceleration Data (ax, ay, az) from IMU sensor during robot operation"
  - file: "/assets/images/projects/advancedmechatronics/gyroscope-plot.html"
    description: "Interactive Gyroscope Data (gx, gy, gz) from IMU sensor during robot operation"
  - file: "/assets/images/projects/advancedmechatronics/speed-controller-plot.html"
    description: "Interactive Speed Controller Data - Left and Right wheel delta values showing motor response and synchronization"
  - file: "/assets/images/projects/advancedmechatronics/accel-tests-plot.html"
    description: "Interactive Acceleration Tests - Complete IMU data including wheel counts and acceleration/gyroscope readings"

# Project Overview
overview: |
  ## Autonomous Container Handling Swarm System (ACHSS)
  
  This Advanced Mechatronics course culminates in a comprehensive multi-phase project focused on designing an autonomous swarm robotics system for container handling at cargo ports. The project spans three integrated phases, each building upon previous designs and learnings.
  
  ### Project Context
  
  Global cargo ports handle millions of TEUs (Twenty-foot Equivalent Units) annually. Modern ports utilize Ship-to-Shore (STS) cranes and fleet logistics with reach stackers and forklifts. This project explores autonomous robotic swarm systems as an innovative approach to streamline port operations and yard logistics.
  
  ### Project Phases
  
  #### Phase 1 - Pandebono (Mini Project 1)
  **Inaugural Propeller-Based Robotic Platform**
  
  The first phase introduces the foundational design concept for the swarm system. Pandebono represents the initial prototype development of a propeller-driven autonomous robot.
  
  **Key Design Elements:**
  - Propeller-based locomotion system
  - Foundational platform architecture
  - Basic autonomous control mechanisms
  - Initial proof-of-concept design
  
  **Deliverables:**
  - Detailed mechanical design documentation
  - CAD models with full assembly
  - Bill of Materials (BOM) for component procurement
  - Hardware diagrams and electrical schematics
  
  #### Phase 2 - Mate (Mini Project 2)
  **Propeller-Based Two-Wheel Autonomous Robot**
  
  Building on Phase 1 learnings, Phase 2 introduces the refined "Mate" robot design. This phase focuses on improving locomotion efficiency, control systems, and multi-robot coordination capabilities.
  
  **Key Improvements:**
  - Optimized two-wheel propeller configuration
  - Enhanced mechanical efficiency
  - Improved autonomous control algorithms
  - Swarm coordination preparation
  
  **Design Features:**
  - Refined propulsion system design
  - Integrated sensor suite for autonomous navigation
  - Power management and battery systems
  - Structural optimization for durability
  
  **Deliverables:**
  - Complete mechanical design with improvements
  - 3D CAD models and assemblies
  - Updated Bill of Materials
  - Performance analysis and testing results
  - Control system documentation
  
  #### Phase 3 - Integrated System
  **Complete Autonomous Container Handling Swarm System**
  
  The final phase integrates all subsystems into a complete, operational swarm robotics platform. This includes multiple robot units, centralized coordination system, container tracking, and port integration capabilities.
  
  **System Integration:**
  - Multi-robot swarm coordination
  - Centralized command and control system
  - Container identification and tracking
  - Fleet-level logistics management
  - Port integration interfaces
  
  **Advanced Features:**
  - Swarm intelligence algorithms
  - Real-time path planning and collision avoidance
  - Container load balancing across fleet
  - Energy-efficient operation
  - Scalable architecture for fleet expansion

# System Architecture
architecture: |
  ## Mechanical Design
  
  ### Propulsion Systems
  - **Motor Type**: High-efficiency brushless motors
  - **Transmission**: Direct-drive propeller configuration
  - **Control**: Electronic speed controllers (ESC)
  - **Power Source**: LiPo batteries with management systems
  
  ### Chassis & Structure
  - **Frame Material**: Lightweight composite/aluminum construction
  - **Dimensions**: Optimized for port navigation and obstacle avoidance
  - **Structural Integrity**: FEA-optimized for durability
  
  ### Sensor Suite
  - **Positioning**: GPS + Local navigation sensors
  - **Obstacle Detection**: LiDAR/Ultrasonic sensors
  - **Container Detection**: Computer vision systems
  - **Inertial Measurement**: IMU for stability control
  
  ## Control Systems
  
  ### Autonomous Control
  - Real-time path planning algorithms
  - Adaptive control for terrain and load variations
  - Collision avoidance and safety systems
  - Individual robot autonomy
  
  ### Swarm Coordination
  - Distributed communication protocols
  - Consensus algorithms for fleet coordination
  - Task allocation and scheduling
  - Load balancing across multiple units
  
  ### Integration
  - Communication interface with port infrastructure
  - Fleet management dashboard
  - Real-time monitoring and telemetry
  - Emergency override and safety protocols

# Project Specifications
specifications:
  - "Autonomous propeller-based robotic platform with efficient locomotion"
  - "Multi-phase iterative design optimization (Pandebono → Mate → Integrated System)"
  - "Swarm robotics with coordinated multi-robot operation"
  - "Container handling and port logistics automation"
  - "Real-time autonomous navigation and path planning"
  - "Comprehensive sensor integration (GPS, LiDAR, vision, IMU)"
  - "Battery-powered autonomous operation"
  - "Scalable fleet architecture"
  - "Safety systems with collision avoidance"
  - "Integration with port infrastructure"

# Key Features
features:
  - "Three progressive design iterations with increasing complexity"
  - "Production-ready mechanical design documentation"
  - "Complete CAD models for all project phases"
  - "Detailed Bill of Materials with component specifications"
  - "Hardware diagrams and electrical schematics"
  - "Autonomous navigation and control systems"
  - "Multi-robot swarm coordination capabilities"
  - "Real-time monitoring and fleet management"
  - "Scalable architecture for fleet expansion"

# Technologies Used
technologies:
  - "3D CAD Software (Fusion 360 / Autodesk Inventor)"
  - "FEA & Structural Analysis"
  - "Propeller-based propulsion systems"
  - "Brushless motor control (ESC)"
  - "LiPo battery management"
  - "Real-time embedded systems"
  - "ROS (Robot Operating System) for swarm coordination"
  - "Autonomous navigation algorithms"
  - "Computer vision and LiDAR processing"
  - "Wireless communication protocols"
  - "glTF 2.0 format for 3D model visualization"

# Design Outputs
design_outputs: |
  ## Deliverables
  
  ### Documentation
  - Comprehensive project reports for each phase
  - Design proposals and feasibility studies
  - System architecture documentation
  - Control system specifications
  
  ### 3D Models & CAD
  - Complete CAD assemblies for all phases
  - Individual component drawings with tolerances
  - Assembly instructions and exploded views
  - Interactive 3D models in glTF format with colors and materials
  
  ### Engineering Specifications
  - Detailed Bill of Materials (BOM)
  - Hardware electrical diagrams
  - Sensor integration specifications
  - Power management calculations
  
  ### Analysis & Testing
  - Structural analysis results (FEA)
  - Performance simulations
  - Testing and validation reports
  - Design iteration documentation

# Sensor Data Analysis
sensor_analysis: |
  ## IMU Data Collection and Analysis
  
  The autonomous robots are equipped with Inertial Measurement Units (IMU) for real-time monitoring of motion dynamics. The sensor data includes:
  
  ### Acceleration Data (ax, ay, az)
  Measured in m/s², capturing linear acceleration across three axes:
  - **ax**: Acceleration along x-axis (forward/backward)
  - **ay**: Acceleration along y-axis (left/right)
  - **az**: Acceleration along z-axis (vertical)
  
  These measurements are critical for:
  - Detecting collision impacts
  - Monitoring traction and slip conditions
  - Validating terrain response
  - Calibrating autonomy algorithms
  
  ### Gyroscope Data (gx, gy, gz)
  Measured in °/s (degrees per second), capturing angular velocity:
  - **gx**: Rotation rate around x-axis (pitch)
  - **gy**: Rotation rate around y-axis (roll)
  - **gz**: Rotation rate around z-axis (yaw)
  
  These measurements provide:
  - Orientation tracking and stabilization
  - Turn rate validation
  - Tumble/tilt detection
  - Path correction feedback
  
  ### Interactive Visualization
  Explore the real sensor data from robot operation using the interactive plots below. Hover over the graphs to see exact values at each sample point. The plots show 840 data samples collected during autonomous operation testing.
  
  #### Acceleration Plot (ax, ay, az)
  - Red line: X-axis acceleration
  - Green line: Y-axis acceleration  
  - Blue line: Z-axis acceleration
  
  #### Gyroscope Plot (gx, gy, gz)
  - Red line: X-axis angular velocity (pitch)
  - Green line: Y-axis angular velocity (roll)
  - Blue line: Z-axis angular velocity (yaw)
  
  These plots are interactive - zoom, pan, and hover to explore the sensor data in detail.
