---
layout: project
title: "LeRobot Hackathons - VLA Models for SO-100"
subtitle: "Vision-Language-Action Models for Robotic Manipulation"
description: "Hackathon projects using VLA and VLM models with SO-100 robot: shorts folding, kitchen tasks with Moondream, and plantain leaf cleaning"
date: 2025-06-01
categories: [Robotics, Machine Learning, VLA, Vision-Language Models, LeRobot]
authors: ["Alejandro Ojeda Olarte"]
institution: "Independent Research"
featured_image: "/assets/images/projects/lerobot-hackathons/LeRobotGlobal.gif"

technologies:
  - Vision-Language-Action Models (VLA)
  - Moondream VLM
  - SO-100 Robot
  - LeRobot Framework
  - PyTorch
  - Imitation Learning

gallery:
  - file: "/assets/images/projects/lerobot-hackathons/LeRobotGlobal.gif"
    description: "LeRobot hackathon overview - VLA models in action"
  - file: "/assets/images/projects/lerobot-hackathons/PXL_20250420_2133288442.gif"
    description: "SO-100 robot manipulation demonstration"
  - file: "/assets/images/projects/lerobot-hackathons/PXL_20250615_165501885.gif"
    description: "Kitchen manipulation tasks with Moondream VLM"
  - file: "/assets/images/projects/lerobot-hackathons/PXL_20251231_140958304 (1).gif"
    description: "Plantain leaf cleaning - cultural task adaptation"
  - file: "/assets/images/projects/lerobot-hackathons/PXL_20250420_213328844~2.mp4"
    description: "Full demonstration video"
---

## Project Overview

Participation in **LeRobot hackathons** exploring **Vision-Language-Action (VLA) models** and **Vision-Language Models (VLM)** for robotic manipulation with the **SO-100 robot**. Three progressive projects demonstrating cloth manipulation, kitchen tasks, and cultural task adaptation.

### Hackathon Projects

1. **Shorts Folding** - VLA models for deformable object manipulation
2. **Kitchen Tasks with Moondream** - VLM-guided navigation, cleaning, and utensil manipulation  
3. **Plantain Leaf Cleaning** - Cultural adaptation for Colombian culinary traditions

---

## What are Vision-Language-Action Models?

**VLA models** combine vision, language understanding, and robotic control in a single end-to-end system:

- **Vision**: Camera input for scene perception
- **Language**: Natural language task instructions
- **Action**: Direct robot control commands

This enables robots to understand tasks from human descriptions and execute them using visual feedback.

---

## Hackathon 1: Shorts Folding

**Challenge**: Fold shorts using VLA models - a classic deformable object manipulation task.

**Approach**:
- Imitation learning from teleoperated demonstrations
- Vision encoder + language instruction encoder → action policy
- Trained on SO-100 robot kinematics

**Key Skills**: Cloth state perception, grasp point detection, sequential folding actions

---

## Hackathon 2: Kitchen Manipulation with Moondream

**Moondream VLM** is a lightweight vision-language model providing scene understanding and spatial reasoning.

### Tasks Completed:

#### Navigation
Navigate kitchen using natural language: "Go to the sink", "Move to the countertop"

#### Countertop Cleaning
Visual inspection → dirt detection → wiping trajectory → execution

#### Fork & Utensil Manipulation
- Grasp forks from various orientations
- Precise placement and organization
- Sorting by type

#### Table Cleaning
Object detection → removal planning → surface wiping → verification

---

## Hackathon 3: Plantain Leaf Cleaning

### Cultural Context

In Colombian cuisine, **plantain leaves** wrap tamales and traditional dishes. They must be cleaned carefully before use.

### Challenge

Adapt learned manipulation skills to clean large, flexible plantain leaves without tearing them.

**Approach**:
- Gentle edge grasping
- Adaptive force control
- VLM-guided inspection: "Is this area clean?", "Where is the dirt?"

**Impact**: Demonstrates how robotic systems can adapt to culturally-specific tasks.

---

## Technical Stack

**Frameworks**:
- LeRobot - Robot learning framework
- PyTorch - Deep learning
- Moondream - Vision-language model

**Robot**: SO-100 (6 DOF + gripper, ~500mm reach)

**Training**: Behavior cloning from human demonstrations

---

## Key Learnings

✅ **VLAs simplify pipelines** - Direct vision-to-action mapping  
✅ **Language enables intuition** - Natural task specification  
✅ **Pre-training is powerful** - Vision-language models provide strong priors  
✅ **Cultural relevance matters** - Robotics should serve diverse communities

---

## Resources

- **LeRobot**: [huggingface.co/lerobot](https://huggingface.co/lerobot)
- **Moondream**: [huggingface.co/vikhyatk/moondream2](https://huggingface.co/vikhyatk/moondream2)
- **SO-100 Robot**: Open-source manipulation platform

---

## Keywords

`LeRobot` `Vision-Language-Action` `VLA` `Moondream` `SO-100` `Robotic Manipulation` `Imitation Learning` `Kitchen Robotics` `Cultural Robotics` `Deep Learning` `PyTorch`

---

*Vision, language, and action for intelligent manipulation* 🤖✨
