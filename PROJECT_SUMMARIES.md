# Project Portfolio Summaries - Alejandro Ojeda

## Project 2 (P2) - Redundant Manipulator Control with Collision Avoidance

### Main Subject/Title
**Redundant Manipulator Control and Collision Avoidance for a 4-DOF Robot Arm**

### Objectives and Goals
- Design and implement inverse kinematics control for a redundant 4-degree-of-freedom (4-DOF) manipulator
- Develop a trajectory tracking system using error-based proportional-derivative (PD) control
- Implement collision avoidance mechanisms using null-space projections
- Test and validate the control algorithms with numerical simulations

### Key Methodologies and Approaches

#### 1. **Inverse Kinematics Control**
- Utilized the Jacobian matrix inversion method for kinematic transformations
- Jacobian matrix maps joint velocities to end-effector velocities
- Implementation of full rank Jacobian inverse for the 4-DOF system
- Robot configuration: Two revolute joints (q1, q2) with link lengths a1=0.5, a2=0.5, plus prismatic joint (d3) and rotational joint (q4)

#### 2. **PD Control with Error Feedback**
- **Closed-loop trajectory tracking** using proportional-derivative gains
- Control law: $\ddot{q} = J_A^{-1}(q)(\ddot{x}_d + K_D\dot{e} + K_P e - \dot{J}_A(q, \dot{q})\dot{q})$

- **Derivative Gain Matrix (KD)**:
  - Diagonal matrix with values [60, 108, 0.6, 60] for joints 1-4
  
- **Proportional Gain Matrix (KP)**:
  - Diagonal matrix with values [60, 108, 48, 100] for joints 1-4

#### 3. **Null-Space Collision Avoidance**
- Used pseudo-inverse Jacobian ($J_A†$) for redundancy management
- Implemented hierarchical control with primary and secondary tasks
- **Collision avoidance in null-space**:
  - Defined spherical obstacle avoidance zone (center at [0.4, -0.7, 0.5], radius R=0.2)
  - Secondary objective: $\ddot{q}_0 = k_0 \frac{\partial w(q)}{\partial q}$, where $w(q)$ minimizes distance to obstacles
  - Null-space projection ensures primary task (trajectory tracking) is maintained

#### 4. **Technical Implementation**
- MATLAB/Simulink-based simulation environment
- 4x4 Jacobian matrix with reducible configuration
- Kinematic chain: (q1, q2) → planar 2-DOF arm; (d3) → prismatic extension; (q4) → end-effector rotation
- Numerical integration for trajectory generation

### Key Results and Findings
1. **Successful trajectory tracking** with stable error convergence
2. **Effective collision avoidance** in null-space without compromising primary trajectory
3. **Control gain tuning** demonstrated stability trade-offs between responsiveness and oscillation
4. **Redundancy exploitation**: The extra DOF allowed simultaneous tracking and obstacle avoidance

### Important Technical Details and Equations

**Jacobian Configuration (Reduced Form)**:
```
J_A = [-a1*sin(q1)-a2*sin(q1+q2),  -a2*sin(q1+q2),  0,  0]
      [ a1*cos(q1)+a2*cos(q1+q2),   a2*cos(q1+q2),  0,  0]
      [ 0,                          0,              -1,  0]
      [ 0,                          0,               0,  1]
```

**Jacobian Derivative (Coriolis-like terms)**:
```
J_dot = [ a2*sin(q1+q2),    a2*sin(q1+q2),  0,  0]
        [-a2*cos(q1+q2),   -a2*cos(q1+q2),  0,  0]
        [ 0,                0,               0,  0]
        [ 0,                0,               0,  0]
```

**Pseudo-inverse Formulation**:
- $J† = J^T(JJ^T)^{-1}$

### Conclusions
- The redundant 4-DOF arm successfully demonstrated both trajectory tracking and collision avoidance capabilities
- The hierarchical null-space approach effectively separated primary and secondary control objectives
- Control gains and collision avoidance parameters were appropriately tuned for stable operation
- The system shows potential for real-world applications in constrained manipulation tasks

---

## Project 3 (P3) - Trajectory Planning and Robot Dynamics

### Main Subject/Title
**Trajectory Planning with Trapezoidal Velocity Profiles and Dynamics Implementation for a 4-DOF Manipulator**

### Objectives and Goals
- Implement trapezoidal velocity profile trajectory planning for smooth joint motion
- Develop and implement the complete dynamic model of the 4-DOF robot arm
- Integrate trajectory planning with dynamic simulation
- Validate motion planning constraints and physical feasibility

### Key Methodologies and Approaches

#### 1. **Trapezoidal Velocity Profile Planning**
- **Three-phase motion structure**:
  1. **Acceleration phase** (0 ≤ t ≤ tc): Constant acceleration ramp-up
  2. **Constant velocity phase** (tc < t ≤ tf-tc): Linear motion at maximum velocity
  3. **Deceleration phase** (tf-tc < t ≤ tf): Constant deceleration ramp-down

- **Mathematical formulation**:
  - Position: $q(t) = \begin{cases} q_i + \frac{1}{2}\ddot{q}_c t^2 & 0 \leq t \leq t_c \\ q_i + \dot{q}_i t_c(t - \frac{t_c}{2}) & t_c < t \leq t_f - t_c \\ q_f - \frac{1}{2}\ddot{q}_c(t_f - t)^2 & t_f - t_c < t \leq t_f \end{cases}$

- **Velocity constraint verification**:
  - $\frac{|q_f - q_i|}{t_f} < |\dot{q}_c| \leq \frac{2|q_f - q_i|}{t_f}$

#### 2. **Trajectory Parameterization**
- **Path parameterization by arc length (s)**:
  - Position: $p(s) = p_i + s \frac{(p_f - p_i)}{‖p_f - p_i‖}$
  - Velocity: $\dot{p}(s) = \dot{s} t$ (where t is unit tangent vector)
  - Acceleration: $\ddot{p}(s) = \ddot{s} t$

#### 3. **Dynamic Model Implementation**
- **Inertia Matrix (B matrix)** components:
  - Includes link inertias, masses, and kinetic energy terms
  - Accounts for motor inertias and gear ratios (kr values)
  - Coupled terms due to multi-link interactions

- **Representative B-matrix elements**:
  ```
  b11 = Il1 + ml1*l1^2 + kr1^2*Im1 + Il2 + ml2*(a1^2 + l2^2 + 2*a1*l2*cos(q2))
  b12 = Il2 + ml2*(l2^2 + a1*l2*cos(q2)) + kr2*Im2
  ```

- **Coriolis and Centrifugal Matrix (C matrix)**:
  - Contains non-linear coupling terms: $-m_{l2}a_1l_2\sin(q_2)$
  - Represents velocity-dependent interactions between joints
  - Off-diagonal elements couple different joint velocities

- **Friction/Damping Matrix (F matrix)**:
  ```
  F = diag(kr1^2*Fm1, kr2^2*Fm2, kr3^2*Fm3, kr4^2*Fm4)
  ```
  - Gear ratio squared scaling for motor friction
  - Fm represents motor friction coefficients

- **Gravity Vector (g matrix)**:
  ```
  g = [(ml1*l1 + ml2*a1)*9.8*cos(q1) + ml2*l2*9.8*cos(q1+q2);
       ml2*l2*9.8*cos(q1+q2);
       ml3*9.8;
       0]
  ```
  - Accounts for gravitational effects on link masses

#### 4. **Dynamic Equations of Motion**
- **Euler-Lagrange formulation**:
  - $\tau = B(q)\ddot{q} + C(q, \dot{q}) + F\dot{q} + g(q)$
  - Where τ is the torque input vector
  - Solved as: $\ddot{q} = B^{-1}(u - C\dot{q} - F\dot{q} - g)$

#### 5. **Trajectory Execution via MATLAB**
- Trapezoidal profile generator produces reference trajectories
- Dynamic simulation integrates the equations of motion
- Feedback control ensures tracking of planned trajectories

### Key Results and Findings
1. **Smooth trajectory generation** with constrained acceleration/deceleration
2. **Validated velocity constraints** ensuring physical feasibility
3. **Dynamic coupling effects** successfully captured in multi-DOF system
4. **Gravitational compensation** essential for stable low-speed motion
5. **Successful trajectory tracking** despite non-linear dynamics and coupling

### Important Technical Details and Equations

**Trapezoid Profile MATLAB Implementation**:
```matlab
function [T,q,dq,ddq,err] = trapez(q_i,q_f,dq_c,t_f,Ts)
  T = (0:Ts:t_f)';
  delta = q_f - q_i;
  dq_c = sign(delta)*abs(dq_c);
  
  % Validation: velocity must exceed minimum but not exceed maximum
  dq_r = abs(delta/t_f);
  err = (abs(dq_c) <= dq_r)|(abs(dq_c) > 2*dq_r);
  
  % Three-phase profile construction
  t_c = t_f - delta/dq_c;
  ddq_c = dq_c/t_c;
  % ... trajectory computation
end
```

**Robot Parameters Used**:
- Link lengths: a1 = 0.5, a2 = 0.5 m
- Link masses: ml1, ml2, ml3 (variable)
- Link inertias: Il1, Il2, Il3, Il4
- Motor parameters: Motor inertias (Im), gear ratios (kr), motor friction (Fm)
- Gravity constant: g = 9.8 m/s²

### Conclusions
- Trapezoidal velocity profiles provide practical and efficient trajectory planning
- The complete dynamic model successfully captures all physical effects (inertia, coupling, friction, gravity)
- The integration of trajectory planning with dynamics creates a realistic simulation environment
- The system demonstrates feasible motion profiles for industrial manipulator applications

---

## Combined Portfolio Context

### Common Thread
Both projects address fundamental challenges in robotic manipulator control:
- **P2** focuses on the control layer: real-time trajectory tracking with collision avoidance
- **P3** provides the foundation: trajectory planning and dynamic modeling

### Technical Sophistication
- Advanced kinematics and Jacobian-based control
- Non-linear dynamics with coupled multi-joint systems
- Optimization techniques (null-space projection, pseudo-inverse)
- MATLAB/Simulink simulation and implementation

### Potential Applications
- Industrial robot arms with safety requirements
- Autonomous manipulation in constrained environments
- Path planning for redundant manipulators
- Dynamic simulation for robot design validation

---

**Student**: Alejandro Ojeda  
**Course**: Advanced Robotics/Mechatronics (NYU)  
**Project Type**: Research/Design Projects 2 & 3  
**Date**: Academic Year 2024-2025
