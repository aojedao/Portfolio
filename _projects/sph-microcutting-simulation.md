---
layout: project
title: "SPH Microcutting Simulation in LS-DYNA"
subtitle: "Titanium Ti-6Al-4V Micromachining Process Modeling"
author: "Alejandro Ojeda Olarte"
institution: "Universidad Nacional de Colombia"
department: "Departamento de Ingeniería Mecánica y Mecatrónica"
date: 2024-01-01
tags: [Simulation, SPH, Micromachining, LS-DYNA,  Titanium, FEM]
difficulty: Advanced
category: computational-mechanics
featured_image: "/assets/images/projects/sph-microcutting/simulation-1.gif"
---

## Overview

This project presents a comprehensive simulation of a microcutting process on titanium alloy Ti-6Al-4V using the Smoothed Particle Hydrodynamics (SPH) method in LS-DYNA software. The simulation models material removal with a single-edge cutting tool, analyzing the physical behavior of the material during the micromachining process.

![Simulation Process](/assets/images/projects/sph-microcutting/simulation-2.gif)

### Key Features
- **SPH Method**: Advanced particle-based simulation for continuous media
- **Johnson-Cook Model**: Material behavior modeling including strain hardening and thermal softening
- **LS-DYNA Integration**: Professional-grade simulation software
- **Micromachining Analysis**: Study of material removal at micro-scale
- **Thermal Analysis**: Temperature distribution during cutting process

---

## Introduction

Modern industry requires excellent manufacturing processes to obtain products for specific special applications. Size limitations in manufacturing increasingly represent a problem of lesser impact, achieving components at a smaller scale. Consequently, it is necessary to control the parameters that govern these processes, so that the behavior of the base material can be predicted.

This document studies a micro-cutting process with a single-edge tool on a Ti6Al4V titanium alloy. The development of this project is part of the academic training process in the area of micromachining research and is based on the use of a model referenced by Mark J. Jackson.

---

## Objectives

### General Objective
Simulate the material removal process with a single-edge tool on titanium Ti-6Al-4V

### Specific Objectives
- Familiarize with LS-DYNA software for cutting simulation
- Collect data on the Ti-6Al-4V titanium alloy through review of academic documents according to the parameters required by the program
- Model the cutting process on the reference material
- Model the orthogonal micro-cutting process in counter-direction with a single-edge tool

---

## Methodology

The project proposes modeling the material as a group of nodes using SPH, with the tool as a solid element.

### 1. State of the Art Review

The bibliography was reviewed, particularly Mark J. Jackson's work, which proposes modeling the micromachining process using SPH (Smoothed Particle Hydrodynamics), given that this computational method is recommended for continuous elements such as solids or liquids. Additional references included works by Davim and Cai.

### 2. Software Acquisition

The software consists of two parts:
- **LS-PrePost**: Graphical interface for data input
- **LS-DYNA**: Calculation engine for machining simulation

A license was obtained through the local Brazilian distributor after correspondence with the software provider.

### 3. Initial Software Model

A simulation was performed based on a model created by LS, the company that produces the application used in the project. The complete process includes:

1. **Geometry Creation**: Elements, material, and tool
2. **Johnson-Cook Parameters**: Material behavior data input
3. **Thermal Characteristics**: Temperature-dependent properties
4. **LS-DYNA Processing**: Behavioral calculation

![Parameters Diagram](/assets/images/projects/sph-microcutting/parameters-diagram.jpg)

---

## Material Analysis

### Ti-6Al-4V Titanium Alloy Data Collection

Parameters required for simulation execution were reviewed from multiple academic articles. This document compiles the information more completely than individual sources.

#### Johnson-Cook Model Parameters

Titanium can be studied using the Johnson-Cook model to understand its strain hardening and thermal expansion. Data analyzed by Vijay were taken as reference to compare practical results with theoretical simulation results.

The Johnson-Cook analysis includes parameters such as:
- Density
- Elastic modulus
- Poisson's ratio
- Specific heat
- Melting point
- Ambient temperature
- Minimum stress for fracture
- Mechanical strength

Material data was compiled from various authors including Vijay, Kiralni, J. Sun, and Kay.

### Process Geometry Definition

![Assembly View](/assets/images/projects/sph-microcutting/assembly.jpg)

Angle of incidence and clearance angle values were taken based on recommendations by Donachie.

**Material dimensions**: 40mm × 20mm × 20mm

**Analyzed cutting parameters**:
- Alpha angle: 11.3°
- Gamma angle: 11.3°
- Beta angle: 67.3°
- Cutting thickness: 3.5mm
- Radius of curvature: 0.3mm

Important aspects studied:
- Feed per tooth
- Cutting speed
- Axial cutting depth

---

## Simulation Results

### Execution Performance

The LS-DYNA execution showed progressive optimization across multiple runs:

| Run | Estimated CPU Time |
|-----|-------------------|
| 1st | 34 hours |
| 2nd | 28 hours |
| 3rd | 22 hours |
| Final | 6 hours |

### Post-Processing Analysis

After loading the d3plot file generated by LS-DYNA into LS-PrePost, various characteristics were analyzed using the Post menu:

- **Plastic Deformation**
- **Temperature Distribution**
- **Stress Analysis**
- **Material Flow**

![Simulation Animation 1](/assets/images/projects/sph-microcutting/simulation-1.gif)

The simulation successfully executed around the material with the objective of familiarizing with the application, showing the behavior of plastic deformation during the process.

---

## Components & Materials

### Software Requirements
- **LS-DYNA**: Explicit dynamics finite element analysis program
- **LS-PrePost**: Pre and post-processor for LS-DYNA
- Operating System: Windows/Linux
- Recommended: Multi-core processor, 16GB+ RAM

### Material Specifications
- **Base Material**: Titanium alloy Ti-6Al-4V
- **Tool Material**: Solid cutting element
- **Simulation Method**: SPH (Smoothed Particle Hydrodynamics)

### Johnson-Cook Model Implementation
```
Material Properties:
- Density: ρ
- Elastic Modulus: E
- Poisson's Ratio: ν
- Specific Heat: Cp
- Melting Temperature: Tm
- Reference Temperature: Tr
```

---

## Technical Specifications

### Cutting Tool Geometry
- Rake angle (α): 11.3°
- Clearance angle (γ): 11.3°
- Wedge angle (β): 67.3°
- Edge radius (rₑ): 0.3mm
- Cut depth: 3.5mm

### Simulation Parameters
- **Method**: SPH nodes for material, solid elements for tool
- **Time Integration**: Explicit dynamics
- **Contact Algorithm**: Penalty-based contact
- **Thermal Coupling**: Coupled thermomechanical analysis

---

## Learning Outcomes

This project provided valuable experience in:

1. **Advanced Simulation Techniques**: Understanding SPH methods for manufacturing processes
2. **Material Modeling**: Implementation of Johnson-Cook constitutive model
3. **Software Proficiency**: LS-DYNA and LS-PrePost workflow
4. **Micromachining Understanding**: Physics of material removal at micro-scale
5. **Computational Optimization**: Reducing simulation time through parameter tuning
6. **Academic Research**: Literature review and data compilation from multiple sources

---

## Future Improvements

Potential enhancements to this project:

- **Equation of State**: Implement complete equation of state for titanium
- **Experimental Validation**: Compare simulation results with actual microcutting experiments
- **Parameter Optimization**: Study effect of different cutting parameters
- **Tool Wear Analysis**: Model tool degradation over time
- **Multi-pass Simulation**: Simulate multiple cutting passes
- **Different Materials**: Extend analysis to other engineering alloys
- **Chip Formation Study**: Detailed analysis of chip morphology

---

## Multimedia Resources

### Simulation Videos
- [Video 1: Full Process](/assets/videos/projects/sph-microcutting/movie_000.avi)
- [Video 2: Detailed View](/assets/videos/projects/sph-microcutting/movie_002.avi)
- [Video 3: Alternative Angle](/assets/videos/projects/sph-microcutting/movie_003.avi)

### Animations
![Plastic Deformation](/assets/images/projects/sph-microcutting/simulation-1.gif)
![Cutting Process](/assets/images/projects/sph-microcutting/simulation-2.gif)

---

## References

This project was developed based on research by:
- Mark J. Jackson - SPH modeling for micromachining processes
- Davim - Machining fundamentals
- Cai - Computational methods in manufacturing
- Vijay - Johnson-Cook parameters for Ti-6Al-4V
- Kiralni - Material behavior modeling
- J. Sun - Titanium alloy properties
- Kay - Thermal characteristics
- Donachie - Tool geometry recommendations
- Yusuf Altintas - Machining parameters

---

## Contact & Attribution

**Author**: Alejandro Ojeda Olarte
**Institution**: Universidad Nacional de Colombia  
**Department**: Ingeniería Mecánica y Mecatrónica

---

## Project Keywords

`SPH` `LS-DYNA` `Micromachining` `Titanium` `Ti-6Al-4V` `Johnson-Cook` `Simulation` `FEM` `Computational Mechanics` `Manufacturing` `Material Removal` `Thermal Analysis` `Plastic Deformation`

---

## License

This project documentation is part of academic research conducted at Universidad Nacional de Colombia. For usage permissions and collaborations, please contact the author.
