---
layout: project
title: "Dual Manipulator Unscrewing Robot - Mobile Torque-Compensated Manipulation in Zero-G"
description: "Simulation and control framework for autonomous On-Orbit Servicing, Assembly, and Manufacturing (OSAM). Dual-arm robotic system with Jacobian-based torque compensation achieving 91% reduction in base angular deviation during high-torque screw extraction in microgravity."
date: 2025-12-08
categories: [Space Robotics, Autonomous Systems, Dual-Arm Manipulation, Zero-G Control, OSAM, MuJoCo Simulation, Motion Planning]
authors: ["Alejandro Ojeda Olarte"]
institution: "NYU - Space Robotics"
featured_image: "/assets/images/projects/space-robotics/SpaceRobotics (1).gif"
github_url: "https://github.com/aojedao/SpaceRobotics7863/tree/main"

technologies:
  - MuJoCo Physics Engine
  - KUKA IIWA 14 (7-DOF Redundant Manipulators)
  - Robotiq 2F85 Gripper
  - Jacobian-Based Control
  - Motion Planning (A* Algorithm)
  - Zero-G Dynamics
  - Python
  - Control Theory

models: []

gallery:
  - file: "/assets/images/projects/space-robotics/Picture1.png"
    description: "Simulation environment - Dual-arm robot performing wall-to-ceiling transition in MuJoCo"
  - file: "/assets/images/projects/space-robotics/Picture2.png"
    description: "Performance data - Base attitude error with and without torque compensation"
  - file: "/assets/images/projects/space-robotics/Picture3.png"
    description: "Step-by-step motion sequence - One arm anchored to ISS handles while approaching next waypoint"
  - file: "/assets/images/projects/space-robotics/SpaceRobotics.gif"
    description: "Full mission demonstration - Navigation and screw extraction task"
  - file: "/assets/images/projects/space-robotics/ezgif-496f20b11beee9.gif"
    description: "Robotic manipulation demonstration in zero-gravity simulation"

---

## Dual Manipulator Unscrewing Robot: Mobile Torque-Compensated Manipulation in Zero-G

### Project Abstract

This project presents a **simulation and control framework** for a dual-arm robotic system designed for autonomous **On-Orbit Servicing, Assembly, and Manufacturing (OSAM)** operations. Operations in microgravity present unique dynamical challenges, particularly the coupling between manipulator motion and the floating base's attitude dynamics.

A **novel control strategy** treats the dual-arm system similar to a bipedal walker, leveraging redundant kinematics to maintain static stability during manipulation. A **Jacobian-based null-space torque compensation controller** minimizes reaction moments at the base, decoupling manipulation forces from base attitude.

**Validated within the MuJoCo physics engine**, the proposed system demonstrates a **91% reduction in base angular deviation** during high-torque screw extraction tasks compared to conventional control methods.

---

## Mission Context & Motivation

### The Challenge

The sustainability of the **cis-lunar economy** and **deep-space exploration** relies heavily on the maturation of **On-Orbit Servicing, Assembly, and Manufacturing (OSAM)** capabilities. Currently, the deployment and maintenance of space infrastructure, such as the **International Space Station (ISS)**, depend on tasks performed by astronauts.

**Key Issues**:
- Operations cost approximately **$150,000 per hour**
- Complexity of modern experiments exceeds human endurance limits
- Critical need for autonomous systems for intricate assembly tasks
- Examples: Installation of EXPRESS Racks, reconfiguration of BLiSS Rack stacks

### Why Autonomous Robots?

Transitioning from **teleoperated arms** (e.g., Canadarm2) to **autonomous free-floating robots** enables:
- ✅ Cost reduction through automation
- ✅ Precise, repeatable manipulation beyond human capability
- ✅ 24/7 operation without astronaut EVA time
- ✅ Support for complex ISS experiments and deep-space missions

---

## Technical Approach & Innovation

### System Architecture

The system is modeled as a **floating base B** equipped with **two 7-DOF redundant manipulators**:
- **Left Manipulator**: KUKA IIWA 14 with Robotiq 2F85 Gripper
- **Right Manipulator**: KUKA IIWA 14 with Robotiq 2F85 Gripper
- **Base**: Free-floating in zero-gravity (simulated with MuJoCo, g = 0)

### Core Innovation: Jacobian-Based Torque Compensation

The primary innovation is a **minimization objective for base reaction moments** leveraging redundant manipulator kinematics.

**The Problem**: High-torque tasks (unscrewing, assembly) induce reaction moments that destabilize the floating base.

**The Solution**: Project compensating control inputs into the null-space of the primary task:

$$\dot{q} = J^\dagger \dot{x} + \alpha(I - J^\dagger J)\nabla h$$

Where:
- $J^\dagger$ = pseudo-inverse of the Jacobian matrix
- $\dot{x}$ = desired end-effector velocity
- $\nabla h$ = gradient of secondary task (torque minimization)
- $(I - J^\dagger J)$ = null-space projector

**Cost Function**:

$$h(q) = \frac{1}{2}(\tau_7 - M_b(q))^2$$

Where:
- $\tau_7$ = torque generated by wrist rotation during unscrewing
- $M_b(q)$ = torque projected from end-effector to base frame

The cost function allows the **anchoring arm to dynamically adjust its posture**, absorbing reaction forces and maintaining base stability in a **moment-neutral state**.

### Bipedal Locomotion Framework

The robot treats its grab-points as **"footsteps" on the ISS wall**, enabling autonomous wall crawling:

1. **Wall Discretization**: Continuous wall surface discretized into handle positions with 0.5m spacing
2. **Graph Search**: Motion planning formulated as graph search problem
3. **A* Algorithm**: Optimal sequence of footsteps from start to target screw
4. **Heuristic Function**: Euclidean distance to goal

**Execution Strategy**:
- One arm maintains rigid grasp (provides fixed base for floating base stability)
- Other arm executes redundant controller to approach screw position
- Transition between grasps when waypoints reached

---

## System Dynamics Modeling

The equations of motion for the dual-arm system in the MuJoCo simulation:

$$M(q)\ddot{q} + C(q,\dot{q})\dot{q} + D(q)\dot{q} = \tau - J^T(q)F_{ext}$$

Where:
- $M(q)$ = inertia matrix
- $C(q,\dot{q})$ = Coriolis and centrifugal terms
- $D(q)$ = damping terms
- $F_{ext}$ = external contact forces (wall reaction forces)

**Zero-gravity environment**: Gravitational terms eliminated (g = 0)

---

## Results & Validation

### Experimental Setup

**Test Mission**: 
- Environment: Zero-G ISS module simulation
- Path: 3-meter section of module wall
- Primary Task: Extract standard interface screw

### Base Stability Results

**Performance Comparison**:
- **Without Compensation**: Constant torque reflection at base from screwdriver end-effector
- **With Torque Compensation**: Active reduction to near-zero base reaction moment
- **Achievement**: **91% reduction in base angular deviation**

### Task Completion

- **Alignment Convergence**: Position error < 0.5 cm
- **Robust Tracking Performance**: Consistent across multiple mission scenarios
- **Stability Maintenance**: Base attitude remained stable throughout manipulation

### Key Performance Metrics

| Metric | Without Compensation | With Compensation | Improvement |
|--------|---------------------|-------------------|-------------|
| Base Angular Deviation | 100% | 9% | 91% reduction |
| Task Completion Rate | 85% | 96% | +11% |
| Convergence Time | ~45s | ~35s | 22% faster |

---

## Related Work & Technical Context

### Historical Background

Space robotics traditionally focused on two architectures:
1. **Large Flexible Manipulators**: Berthing operations (Canadarm2, JEMRMS)
2. **Small Free-Flying Inspectors**: Perception drones (Astrobee, JAXA's INT-Ball)

### Recent Advancements

- **GITAI**: Demonstrated dual-arm systems performing dexterous tasks outside ISS
- **Control Research**: Addressing non-holonomic constraints of free-floating bases
- **Simulation Tools**: NVIDIA Isaac, MuJoCo Playground enabling advanced policy validation
- **Learning Approaches**: Reinforcement Learning for motion planning in free-floating environments

### Technical Gap Addressed

**Previous Limitation**: Reaction-null control strategies suffer from:
- Kinematic singularities when null-space is exhausted
- Complex actuator compensation requirements

**This Work**: Overcomes limitations with dynamic null-space projection enabling stable high-torque manipulation.

---

## Control System Architecture

### Primary Task Controller
- **Objective**: End-effector positioning and screw extraction
- **Method**: Inverse kinematics with Jacobian transpose control
- **Loop Rate**: Real-time MuJoCo simulation

### Secondary Task Controller (Torque Minimization)
- **Objective**: Minimize base reaction moments
- **Method**: Null-space projection of torque minimization gradient
- **Priority**: Secondary (non-interference with primary task)

### Motion Planning Layer
- **Algorithm**: A* Search on discretized ISS wall topology
- **State Space**: 3D position of each arm end-effector
- **Planning Horizon**: Full mission trajectory from start to screw

### Safety Systems
- **Joint Limits**: Enforced throughout trajectory
- **Singularity Avoidance**: Monitor Jacobian condition number
- **Contact Detection**: Prevent collisions with ISS structure

---

## Implementation Details

### Software Framework

- **Simulation Engine**: MuJoCo (Physics-accurate zero-G environment)
- **Language**: Python
- **Control Libraries**: NumPy, SciPy for matrix operations
- **Visualization**: Real-time rendering of manipulation tasks

### Robot Parameters

**KUKA IIWA 14 Specifications**:
- **DOF**: 7 (redundant for 6D end-effector pose)
- **Reach**: 800 mm
- **Payload**: 14 kg (nominal, adjusted for zero-G)
- **Control**: Joint torque commands

**Robotiq 2F85 Gripper**:
- **Max Grip Force**: 235 N
- **Stroke**: 85 mm
- **Control**: Grasp force feedback

### Computational Requirements

- **Simulation Frequency**: 1000 Hz
- **Control Loop**: 100 Hz
- **Planning**: ~2-5 seconds for typical missions
- **Hardware**: Standard PC (Intel i3, NVIDIA GPU optional)

---

## Mission Profile: ISS Screw Extraction

### Phase 1: Initialization & Navigation
1. Robot enters ISS module at designated airlock
2. Scan available handles/attachment points
3. Plan optimal path to target screw location

### Phase 2: Wall Crawling
1. Grasp initial handle with left arm
2. Plan waypoint sequence using A* algorithm
3. Execute reaching motions to next grasp points
4. Transition grasps maintaining dynamic stability

### Phase 3: Approach & Alignment
1. Right arm approaches screw position
2. Vision-based alignment (simulated)
3. Converge to contact within 0.5 cm error

### Phase 4: Screw Extraction
1. Gripper closes around screw head (torque-controlled)
2. Apply rotation torque while left arm compensates
3. Monitor base reaction moments (maintain < 0.1 Nm)
4. Extract screw with linear translation

### Phase 5: Completion & Documentation
1. Place screw in secure container
2. Log mission completion and performance metrics
3. Return to neutral configuration

---

## Artificial Intelligence Usage

This project incorporated AI tools in specific capacities:

- **Documentation & Writing**: Google Gemini 3 improved technical writing clarity
- **Jacobian Controller Implementation**: Anthropic Claude Haiku 4.5 optimized control algorithms
- **A* Algorithm & Trajectory Assembly**: Anthropic Claude Opus 4.5 implemented motion planning logic

**Note**: All primary algorithms, control strategies, and system architecture decisions were developed by the researcher. AI tools enhanced implementation quality and documentation.

---

## Future Work & Extensions

### Enhanced Capabilities

1. **Real Hardware Implementation**
   - Test on Astrobee free-flying platform
   - Validate zero-G predictions with actual ISS operations
   - Integrate with ISS robotic systems

2. **Advanced Manipulation Tasks**
   - Complex assembly operations (connector insertion, panel installation)
   - Deformable object handling (cable routing, membrane deployment)
   - Cooperative tasks with multiple robots

3. **Learning & Adaptation**
   - Reinforcement learning for improved torque compensation
   - Transfer learning from simulation to real hardware
   - Online adaptation to unknown ISS geometries

4. **Sensor Integration**
   - Force/torque sensing for contact stability
   - Vision-based grasp point detection
   - Pose estimation for autonomous navigation

5. **Next-Generation Systems**
   - Integration with larger robotic platforms
   - Autonomous satellite servicing missions
   - Deep-space assembly and construction

---

## References

1. ISS National Laboratory, "Facilities: Expedite the processing of experiments to the space station," Accessed: 2025-12-08. [Online]. Available: https://issnationallab.org/facilities/

2. Authors, "Recreation of express rack for space applications," in AIAA Scitech Forum, 2024.

3. NASA, "BLiSS Rack Stack Final Report," NASA Technical Reports Server, 2025.

4. JAXA, "Int-ball: Introduction of an internal drone camera to the international space station," IEEE Xplore, 2024.

5. GITAI, "GITAI completes fully successful technology demonstration outside the ISS," 2024.

6. Flores-Abad, A., et al., "A review of space robotics autonomous control," Progress in Aerospace Sciences, vol. 68, pp. 1–26, 2014.

7. "A review of spatial robotic arm trajectory planning," Aerospace, vol. 9, no. 7, p. 361, 2022.

8. Authors, "Motion planning and reinforcement learning for free-floating space robots," ScienceDirect, 2024.

9. NVIDIA, "Advancing robotic assembly with a novel simulation approach using NVIDIA Isaac," 2023.

10. DeepMind, "MuJoCo Playground: An open-source physics simulation environment," arXiv preprint arXiv:2502.08844, 2025.

11. "A reaction-null/jacobian transpose control strategy with gravity gradient compensation for on-orbit space manipulators," Acta Astronautica, 2014.

12. Sciavicco, L., and Siciliano, B., "Modelling and control of robot manipulators." Springer Science & Business Media, 2012.

---

## Keywords

`Space Robotics` `OSAM` `Dual-Arm Manipulation` `Jacobian Control` `Torque Compensation` `Zero-G Dynamics` `Motion Planning` `MuJoCo` `Autonomous Systems` `ISS` `Control Theory` `On-Orbit Servicing`

---

*Advanced autonomous control for space infrastructure maintenance and deep-space exploration* 🛰️🤖
