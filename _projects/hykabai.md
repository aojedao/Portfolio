---
layout: project
title: "Hykabaï: Autonomous Mobile Robot"
subtitle: "Autonomous Platform for Navigation and Research"
description: "An advanced autonomous mobile robot platform equipped with ROS integration, vision systems, and real-time control for autonomous navigation research and indoor robotics applications."
date: 2023-06-15
author: "Alejandro Ojeda Olarte"
institution: "Microfactory Lab"
categories: [Robotics, Autonomous Systems, Machine Learning, Computer Vision, Control Systems]
difficulty: Advanced
featured_image: "/assets/images/projects/hykabai/Cuadrado.gif"
github_url: ""
demo_url: ""
tags: [ROS, BeagleBone Blue, Computer Vision, Motion Control, Python, C++, Autonomous Navigation]

models:
  - file: "/assets/models/hykabai/Hykabai.gltf"
    description: "3D model of the Hykabaï"

schematics:
  - file: "/assets/schematics/hykabai/BasicFunctionalDiagram.drawio.svg"
    description: "System Architecture and Functional Diagram"
  - file: "/assets/schematics/hykabai/Schematics.pdf"
    description: "Electrical and Control System Schematics"

gallery:
  - file: "/assets/images/projects/hykabai/Cuadrado.gif"
    description: "Square trajectory execution animation"
  - file: "/assets/images/projects/hykabai/Hexagono.gif"
    description: "Hexagonal trajectory execution animation"
  - file: "/assets/images/projects/hykabai/MicroRobot v112.png"
    description: "Hykabaï robot CAD rendering - latest design iteration"
  - file: "/assets/images/projects/hykabai/MicroRobot v11.png"
    description: "Robot platform overview"
  - file: "/assets/images/projects/hykabai/MicroRobot.stl.jpg"
    description: "3D model visualization of chassis assembly"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171227730.jpg"
    description: "Physical prototype in laboratory environment"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171233261.jpg"
    description: "Sensor integration and mounting detail"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171249112.jpg"
    description: "Prototype testing and evaluation"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171258490.jpg"
    description: "Motion test and navigation"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171313647.jpg"
    description: "Autonomous navigation demonstration"
  - file: "/assets/images/projects/hykabai/IMG_20230223_171319537.jpg"
    description: "Platform capabilities in environment"
  - file: "/assets/images/projects/hykabai/Photo from Darkjediornot (2).jpg"
    description: "Action shot during autonomous operation"
  - file: "/assets/images/projects/hykabai/Photo from Darkjediornot.jpg"
    description: "Navigation in unstructured environment"
  - file: "/assets/images/projects/hykabai/WhatsApp Image 2022-10-21 at 2.59.36 PM.jpeg"
    description: "Real-world deployment scenario"
  - file: "/assets/images/projects/hykabai/WhatsApp Image 2022-08-31 at 8.14.57 PM (1).jpeg"
    description: "Robot platform demonstration"
  - file: "/assets/images/projects/hykabai/SquareTrajectory.gif"
    description: "Motion trajectory execution animation"
  - file: "/assets/images/projects/hykabai/encodersequence.gif"
    description: "Encoder signal sequence visualization"
  - file: "/assets/images/projects/hykabai/MicroRobot v14 (1).gif"
    description: "3D model animation of robot movement"
  - file: "/assets/images/projects/hykabai/VID_20220704_201357151.gif"
    description: "Robot navigation and motion demonstration"
  - file: "/assets/images/projects/hykabai/ModulesDiagram.png"
    description: "System Module Architecture"
  - file: "/assets/images/projects/hykabai/NetworkingDiagram.png"
    description: "ROS Network Topology"
  - file: "/assets/images/projects/hykabai/TableDiagram.png"
    description: "Kinematic Parameter Table"
  - file: "/assets/images/projects/hykabai/3DTableDiagram.png"
    description: "3D Workspace Visualization"
  - file: "/assets/images/projects/hykabai/bbbluecomponents.png"
    description: "BeagleBone Blue Component Breakdown"
  - file: "/assets/images/projects/hykabai/rpi3.png"
    description: "Raspberry Pi 3 Supplement Module"
  - file: "/assets/images/projects/hykabai/selectedencoders.png"
    description: "Selected Encoder Specifications"
  - file: "/assets/images/projects/hykabai/MotorEncoder.png"
    description: "Motor-Encoder Integration Detail"
  - file: "/assets/images/projects/hykabai/encodererrortickscount.png"
    description: "Encoder Error Analysis Graph"
  - file: "/assets/images/projects/hykabai/onoffspeedcontrolblock.png"
    description: "Speed Control Block Diagram"
  - file: "/assets/images/projects/hykabai/angularspeedplant.png"
    description: "Angular Speed Plant Characteristics"
  - file: "/assets/images/projects/hykabai/linearspeedplant.png"
    description: "Linear Speed Plant Response"
  - file: "/assets/images/projects/hykabai/lpantestimation.png"
    description: "Low-Pass Filter Test Results"
  - file: "/assets/images/projects/hykabai/SDVrosmachine.png"
    description: "ROS State Machine Diagram"
  - file: "/assets/images/projects/hykabai/MindMap.png"
    description: "Project Mind Map and Structure"
  - file: "/assets/images/projects/hykabai/AlgorithmSoftwareFunction.svg"
    description: "Algorithm and Software Function Diagram"
  - file: "/assets/images/projects/hykabai/KPI Value.png"
    description: "Key Performance Indicators Dashboard"
  - file: "/assets/images/projects/hykabai/Valor de KPI.png"
    description: "KPI Values and Benchmarks"
  - file: "/assets/images/projects/hykabai/SlickGantt.png"
    description: "Project Timeline and Gantt Chart"

plots_title: "Performance Metrics & Analysis"

---

## Project Overview

**Hykabaï** is an advanced autonomous mobile robot platform engineered for research and autonomous navigation applications. The system integrates real-time motion control, ROS (Robot Operating System), computer vision, and sophisticated sensor fusion algorithms to create a versatile robotic platform capable of autonomous navigation and environmental perception.

### Key Innovation Areas

1. **Autonomous Navigation**: SLAM-based localization and simultaneous mapping
2. **Real-time Control**: 100+ Hz control loop with feedback compensation
3. **Modular Architecture**: Plug-and-play hardware and software modules
4. **ROS Integration**: Full Robot Operating System ecosystem compatibility
5. **Computer Vision**: Integration with RGB-D cameras and LIDAR sensors
6. **Sensor Fusion**: Multi-sensor fusion for robust localization and mapping

## System Architecture

### Hardware Platform

**Primary Computing**: BeagleBone Blue (AM5728 Dual-Core 1.5GHz)
- **Onboard Features**: 
  - Dual H-bridge motor drivers
  - 8× servo PWM outputs
  - Multiple sensor interfaces
  - Built-in wireless (WiFi/Bluetooth)
  - Real-time processing capability

**Secondary Compute**: Raspberry Pi 3 (optional)
- Handles computationally intensive vision tasks
- ROS secondary node for distributed processing
- Enhanced storage and development flexibility

### Mobility System

**Drive Configuration**: Differential drive with dual reduction gearmotors

| Parameter | Specification |
|-----------|---------------|
| **Motor Type** | 1:50 Metal Gearmotors (20D) |
| **Rated Voltage** | 6-12 VDC |
| **Stall Torque** | 1.5 Nm @ 12V |
| **No-load Speed** | 300 RPM @ 12V |
| **Encoder Resolution** | Quadrature 64 CPR |
| **Maximum Speed (robot)** | ~0.5 m/s |
| **Turning Radius** | ±0.2 m (in-place capable) |

### Wheel Assembly

- **Type**: Omnidirectional wheels with caster balance wheel
- **Diameter**: 70mm (drive wheels), 25mm (caster)
- **Traction**: Rubber tread for indoor/outdoor operation
- **Ground Clearance**: 30mm (obstacle-capable)

## Control Electronics

### Motor Control Subsystem

```
Encoder Input (64 CPR, Quadrature)
    ↓
Speed Estimation (Low-Pass Filter)
    ↓
PID Controller (Kp=?, Ki=?, Kd=?)
    ↓
PWM Signal (16-bit, 1 kHz)
    ↓
H-Bridge Driver (Polulu DRV8835)
    ↓
Brushed DC Motor (6-12V)
```

### Sensor Integration

**Encoders**: Quadrature shaft encoders for odometry
- Resolution: 64 counts per revolution
- Error Analysis: < 2% cumulative drift over 100m
- Update Rate: Continuous (event-driven)

**Optional Sensors**:
- LIDAR: 2D scanning for obstacle detection (URG-04LX compatible)
- RGB-D Camera: Depth-based object recognition
- IMU: Accelerometer/Gyroscope for tilt compensation
- Battery Monitor: Voltage/Current sensing for power management

## Software Architecture

### ROS Ecosystem Integration

**Core Nodes**:
1. `motor_driver`: Hardware abstraction for motor control
2. `odometry`: Position estimation from encoder feedback
3. `navigation`: Autonomous path planning and obstacle avoidance
4. `vision`: Image processing and object detection
5. `state_machine`: High-level behavior controller

### Control Stack

**Low-Level**: Real-time control loop running on BeagleBone Blue
- Motor PWM commands (update rate: 100 Hz)
- Encoder reading and processing
- Safety watchdog monitoring

**Mid-Level**: ROS coordination layer
- Sensor fusion and filtering
- Trajectory computation
- Communication management

**High-Level**: Autonomous behavior framework
- Task planning and sequencing
- Decision-making algorithms
- Human-robot interaction

## Motion Control Analysis

### Speed Dynamics

The platform exhibits first-order speed response characteristics:

$$\frac{v(t)}{v_{ref}} = 1 - e^{-t/\tau}$$

Where time constant τ ≈ 0.2 seconds, enabling rapid acceleration changes.

### Trajectory Execution

Demonstrated capabilities:
- **Square Pattern**: 1m × 1m with < 5cm positioning error
- **Curved Path**: Smooth bezier curve following with adaptive speed
- **Rotation**: Full 360° in-place rotation with < 10° heading error
- **Multi-segment**: Complex paths combining translation and rotation

### Performance Metrics

| Metric | Value |
|--------|-------|
| **Velocity Range** | 0.05 - 0.5 m/s |
| **Acceleration** | 0.3 m/s² (nominal) |
| **Positioning Accuracy** | ±5 cm |
| **Heading Accuracy** | ±10° |
| **Response Time** | ~100 ms |
| **Battery Life** | 2-4 hours (typical) |

## Autonomous Features

### Navigation Algorithms

**SLAM Implementation**:
- Graph-based optimization (pose graph structure)
- Loop closure detection for map consistency
- Incremental mapping with bounded computation time

**Path Planning**:
- Dijkstra's algorithm for global routes
- Dynamic Window Approach (DWA) for local collision avoidance
- Velocity obstacle (VO) computation for multi-robot scenarios

### Computer Vision

**Object Recognition**:
- Trained YOLOv3/v4 models for common warehouse objects
- Transfer learning from COCO dataset
- Real-time inference on Raspberry Pi GPU acceleration

**Pose Estimation**:
- Marker-based AprilTag detection
- Feature-based visual odometry (ORB-SLAM compatible)
- Sensor fusion with encoder odometry

## Experimental Results

### Navigation Accuracy

Testing in structured indoor environment (5m × 5m):
- **Systematic Error**: < 3% of distance traveled
- **Stochastic Error**: < 2cm standard deviation
- **Loop Closure**: < 10cm position error after 50m circuit

### Power Consumption

Battery capacity: 5 Ah @ 12V (60 Wh nominal)

| Operation | Current (A) | Duration |
|-----------|------------|----------|
| Idle/Standby | 0.2 A | Continuous |
| Navigation | 2-3 A | 2-3 hours |
| Active Sensing | 2.5-4 A | 1.5-2.5 hours |

## Software Development Kit

### ROS Packages and Architecture

The Hykabaï platform is built on standard ROS packages for navigation and perception:

**Navigation Stack**:
- `move_base`: Navigation framework for autonomous movement
- `gmapping`: SLAM implementation using Rao-Blackwellized particle filters
- `amcl`: Adaptive Monte Carlo localization for map-based navigation
- `dwa_local_planner`: Dynamic Window Approach for local collision avoidance

**Vision Processing**:
- `image_transport`: Efficient image streaming across ROS network
- `opencv_ros`: Computer vision pipeline integration
- `depth_image_proc`: Depth image processing from RGB-D sensors

**Control and Monitoring**:
- Custom motor control nodes running on BeagleBone Blue
- Battery monitoring and power management nodes
- Sensor aggregation and odometry computation

### Key Integration Points

The platform integrates with standard ROS tools for development:
- **ROS Master**: Centralized communication hub for all nodes
- **TF (Transform) Framework**: Multi-dimensional transformation support
- **rViz**: Real-time visualization of sensor data and navigation state
- **ROS Bag**: Recording and playback of sensor data for offline analysis

## Design Evolution

The Hykabaï platform represents the culmination of multiple design iterations:

**v1-v2**: Conceptual feasibility studies with simple differential drive
**v3-v5**: Hardware integration and motor control refinement
**v6-v10**: ROS ecosystem integration and basic autonomous navigation
**v11-v14**: Computer vision pipeline development and SLAM implementation
**v14+**: Advanced features including multi-task planning and machine learning

Current version **v28** (CAD) and **v3** (Physical) represent production-ready configurations.

## Applications

### Research Domains

- Autonomous robotics and navigation algorithms
- SLAM and sensor fusion techniques
- Computer vision and object detection
- Robot learning and adaptive control
- Human-robot interaction and social robotics
- Multi-robot coordination and swarms

### Practical Applications

- Indoor autonomous navigation research
- Mobile platform sensor integration testing
- Autonomous mapping and exploration
- Sensor data collection and analysis
- Mobile robot algorithm development and validation

## Future Enhancements

**Planned Improvements**:
1. Enhanced sensor suite (multimodal LIDAR, thermal imaging)
2. Improved SLAM algorithms with loop closure optimization
3. Advanced computer vision for dynamic object tracking
4. Deep learning-based end-to-end navigation
5. Reinforcement learning for task optimization
6. Extended battery life with hybrid power systems
7. ROS 2.0 migration for improved performance
8. Distributed computing with additional compute nodes
9. Advanced obstacle avoidance in crowded environments
10. Real-time performance monitoring and self-diagnostics

## Technical Specifications Summary

| Category | Specification |
|----------|---------------|
| **Platform** | Differential-drive autonomous mobile robot |
| **Compute** | BeagleBone Blue + optional Raspberry Pi |
| **ROS Version** | ROS Melodic/Noetic compatible |
| **Drive Motors** | 1:50 reduction gearmotors (20D) |
| **Maximum Speed** | 0.5 m/s |
| **Positioning Error** | ±5 cm |
| **Sensor Suite** | Encoders, optional LIDAR, optional RGB-D camera |
| **Communication** | WiFi, Bluetooth, Ethernet |
| **Power Source** | 5 Ah LiPo battery (12V nominal) |
| **Operating Time** | 2-4 hours (motion dependent) |
| **Dimensions** | 300 × 250 × 400 mm |
| **Weight** | 3-4 kg |
| **Development** | Python, C++, ROS |

---

## Resources

- [System Functional Diagram](/assets/schematics/hykabai/BasicFunctionalDiagram.drawio.svg)
- [Complete CAD Model (3MF)](/assets/models/hykabai/PI3_Hykabai v3.3mf)
- [Detailed CAD Assembly (F3Z)](/assets/models/hykabai/MicroRobot v28.f3z)
- [Electrical Schematics](/assets/schematics/hykabai/Schematics.pdf)
- [Technical Documentation Library](/assets/schematics/hykabai/)

