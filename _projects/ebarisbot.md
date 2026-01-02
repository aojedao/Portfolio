---
layout: project
title: "Ebarisbot: Assistive Transport Robot"
subtitle: "Semi-autonomous Mobile Platform for Elderly Assistance"
description: "A robust mobile robot designed to transport 15kg payloads for users with lumbar limitations, featuring Bluetooth app control and structural steel chassis."
date: 2022-06-29
author: "Alejandro Ojeda Olarte, Group G3A"
institution: "Universidad Nacional de Colombia"
categories: [Robotics, Mechatronics, Assistive Technology, Product Design]
difficulty: Intermediate
featured_image: "/assets/images/projects/ebarisbot/demo.gif"
github_url: ""
demo_url: ""
tags: [Arduino, Mobile Robot, Fusion 360, FEA, Bluetooth, HC-06, App Inventor]

models:
  - file: "/assets/models/ebarisbot/EbarisbotCompleto.gltf"
    description: "Complete assembly of Ebarisbot including steel chassis and 3D printed housings"
  - file: "/assets/models/ebarisbot/ASX1_BaseControl.3mf"
    description: "3D printed base control housing component"

schematics:
  - file: "/assets/schematics/ebarisbot/report.pdf"
    description: "Full Engineering Design Report (Spanish)"
  - file: "/assets/schematics/ebarisbot/screws.pdf"
    description: "Fastener Selection Analysis"

gallery:
  - file: "/assets/images/projects/ebarisbot/demo.gif"
    description: "Ebarisbot functional prototype in operation"
  - file: "/assets/images/projects/ebarisbot/UserPic.png"
    description: "Target user scenario rendering"
  - file: "/assets/images/projects/ebarisbot/Ebarisbot.jpg"
    description: "Final prototype visualization"
  - file: "/assets/images/projects/ebarisbot/protobajafidelidad.jpg"
    description: "Low-fidelity cardboard prototype for ergonomic validation"
  - file: "/assets/images/projects/ebarisbot/DiagramaVelocidades.JPG"
    description: "Velocity Diagram Analysis"
  - file: "/assets/images/projects/ebarisbot/pruebapeso1.jpeg"
    description: "Static load testing (15kg)"
  - file: "/assets/images/projects/ebarisbot/SE.png"
    description: "Electronic System Schematic"
  - file: "/assets/images/projects/ebarisbot/VelProfInicial.png"
    description: "Initial Velocity Profile"
---

## Overview

**Ebarisbot** is an engineering solution developed to address mobility and load-carrying challenges for elderly users, specifically targeting those suffering from lumbar osteomuscular issues (lumbar back pain). The project converts this health necessity into a functional mechatronic system capable of transporting groceries and household items without requiring physical exertion from the user.

Designed by Group G3A at Universidad Nacional de Colombia, the robot meets strict ergonomic requirements, ensuring load accessibility at specific heights to prevent user bending or reaching.

## Key Features

- **High Load Capacity**: Capable of transporting up to **15 kg** of payload.
- **Ergonomic Design**: Fixed payload height of **86.5 cm**, complying with NTC 5693-1 ergonomics standards for accessible reach (approx. 0.25m above the knuckle).
- **Mobile App Control**: Custom Android application developed in **App Inventor**, communicating via **Bluetooth (HC-06)**.
- **Obstacle Avoidance**: Integrated ultrasonic sensor system to detect collisions and stop automatically.
- **Robust Autonomy**: Powered by a 12V 5Ah Lead-Acid battery offering ~2 hours of continuous operation.

<div class="gallery-grid">
  <img src="/assets/images/projects/ebarisbot/protobajafidelidad.jpg" alt="Prototyping Phase" />
  <img src="/assets/images/projects/ebarisbot/pruebapeso1.jpeg" alt="Weight Testing" />
</div>

## Technical Specifications

### Electronics System
*   **Microcontroller**: Arduino UNO (ATmega328P).
*   **Actuation**: DC Gearmotors driven by an **L298N** Dual H-Bridge driver.
*   **Sensors**: **HC-SR04** Ultrasonic sensor for frontal distance measurement (0-4m range).
*   **Connectivity**: **HC-06** Bluetooth module for UART communication with smartphone.
*   **Power**: 
    *   12V 5Ah Lead-Acid Battery (selected for cost/performance ratio).
    *   LM2596 DC-DC Buck converter (12V to 5V) for logic levels.
    *   2A Fuse protection system.

### Mechanical Design
*   **Chassis Structure**: Manufactured using **steel angle profiles**, selected over aluminum for cost-effectiveness and durability.
*   **Top Speed**: 0.48 m/s (designed limit for safety: 1 m/s).
*   **Simulation**: Extensive Finite Element Analysis (FEA) performed in Fusion 360.
*   **Fabrication**: Combination of welded steel structure and **3D printed (PLA)** components for enclosures and aesthetic covers.

## Control Logic & Software

The robot operates on a loop cycle processing inputs from two sources:
1.  **Pilot Input**: Commands received via Bluetooth (Forward, Backward, Left, Right, Stop).
2.  **Safety Override**: The ultrasonic sensor constantly polls distance. If `distance < threshold`, the robot ignores forward commands to prevent collision.

## Engineering Analysis: Torque Profile

During the design phase, it was critical to simulate the torque requirements of the drive shaft to ensure the selected motors could handle the inertia of a 15kg load accelerating. The chart below visualizes the simulated torque profile over time during a standard movement cycle.

<div id="loading-message">Loading analysis data...</div>
<div id="chart-container" style="position: relative; height:400px; width:100%; margin-top: 2rem; margin-bottom: 2rem; display:none;">
    <canvas id="mechanicsChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    async function loadData() {
        try {
            // Fetch the CSV files
            const [timeResponse, torqueResponse] = await Promise.all([
                fetch('/assets/schematics/ebarisbot/data/t.csv'),
                fetch('/assets/schematics/ebarisbot/data/Torque_profile2.csv')
            ]);

            const timeText = await timeResponse.text();
            const torqueText = await torqueResponse.text();

            // Parse CSV (Found to be single line comma separated)
            const timeData = timeText.split(',').map(Number).filter(n => !isNaN(n));
            const torqueData = torqueText.split(',').map(Number).filter(n => !isNaN(n));

            // Downsample if data is too large (> 5000 points)
            const maxPoints = 2000;
            const factor = Math.ceil(timeData.length / maxPoints);
            
            const sampledLabels = timeData.filter((_, i) => i % factor === 0);
            const sampledData = torqueData.filter((_, i) => i % factor === 0);

            // Hide loading, show chart
            document.getElementById('loading-message').style.display = 'none';
            document.getElementById('chart-container').style.display = 'block';

            // Create Chart
            const ctx = document.getElementById('mechanicsChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: sampledLabels.map(t => t.toFixed(2)),
                    datasets: [{
                        label: 'Reduction Shaft Torque (Nm)',
                        data: sampledData,
                        borderColor: 'rgb(255, 99, 132)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        tension: 0.4,
                        borderWidth: 2,
                        pointRadius: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Time (s)'
                            },
                            ticks: {
                                maxTicksLimit: 10
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Torque (Nm)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Simulated Drive Shaft Torque during Acceleration Cycle'
                        }
                    }
                }
            });

        } catch (error) {
            console.error("Error loading data:", error);
            document.getElementById('loading-message').innerText = "Unable to load visualization data.";
        }
    }

    loadData();
</script>

## Project Result

The final prototype successfully met the "Retomake:able" challenge requirements. It demonstrated the ability to carry the full 15kg load over a 12m course, crossing 3mm floor gaps (simulating tiles) without instability. Not only was the functionality achieved, but the user experience was prioritized through a simple, high-contrast mobile interface suitable for the target demographic.

## Resources & Credits

*   **Authors**: Alejandro Ojeda Olarte, Paula Sofía Medina Díaz, María Alejandra Rojas Huertas, Daniel Esteban Bohórquez Cifuentes, Carlos Andrés Arévalo Rojas.
*   **Course**: Applied Engineering Project (Proyecto Aplicado de Ingeniería).
*   **Institution**: Universidad Nacional de Colombia, 2022.

[View Full Report (PDF)](/assets/schematics/ebarisbot/report.pdf)
