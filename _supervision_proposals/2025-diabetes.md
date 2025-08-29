---
title: "Developing a Safe Insulin Dosing Algorithm for Type 1 Diabetes with Reinforcement Learning"
collection: supervision_proposals
permalink: /ideas-projects/2025-diabetes
date: 2025-08-29
excerpt: This project aims to design RL-based control strategies for safe insulin dosing for Type 1 Diabetes (T1D) patients.
---

## Motivation

While PID and MPC controllers are capable of managing insulin delivery for type 1 diabetes (T1D) patients, they often struggle with common disturbances like meals, exercise, and physiological stress. These events introduce significant uncertainty and rapid changes in glucose dynamics that classical control algorithms may not handle effectively, requiring proactive patient intervention to maintain stable blood glucose levels. This project aims to use reinforcement learning (RL) for an insulin delivery controller. The goal is to leverage the adaptability of RL policies to handle patient-specific dynamics, uncertainty, and disturbances. However, a major challenge is ensuring the controller's decisions are (near-)safe and computationally efficient for a small, battery-powered medical device.

<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Blue_circle_for_diabetes.svg/200px-Blue_circle_for_diabetes.svg.png"
        alt="blue circle"
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>A blue circle, the symbol for diabetes. Image is taken from <a href="https://en.wikipedia.org/wiki/Type_1_diabetes">wikipedia.org/...</a></figcaption>
</div>

## Tasks and Timeline

### Stage 1:

* Define the safe reinforcement learning problem in insulin dosing for Type 1 Diabetes;
* Delimitate the solution concept: We aim for a lightweight RL-based control system capable of using notions of risk in its policies for insulin dosing.
* Review the state-of-the-art and proposed solutions in the literature;
* Brainstorm potential solutions for the problem and propose concept designs.

### Stage 2:

* Set up a suitable Type-1 Diabetes simulator environment for experimentation;
* Develop a data and feature pipeline with a focus on a risk notion;
* Implement relevant baselines, from classical control (Model predictive control and PID) to risk-neutral RL algorithms (Q-learning, PPO, ...)
* Design a proof-of-concepts of safe RL-based controllers as potential solutions via minimum viable product concept;

### Stage 3: 

* Plan the experiments and test for the expected solution;
* Propose relevant metrics related to performance, safety, and computational resources, to analyse the experiments.
* Evaluate the proof-of-concept with the proposed experiments and tests;
* Benchmark the proof-of-concept against relevant baselines and other solutions in the literature. 

## Expected Outcomes

### Mandatory Products
* Mathematical analysis of the proposed algorithm;
* Software with documentation associated with the project;
* Technical report with problem description, proposed solutions, experimental results, and project conclusions by following the University guidelines;
* A public dissertation following the University guidelines.

### Optional Products
* Summary paper from the technical report suitable for conferences or journals;
* 3-minute elevator pitch video of the project;
* Blog post or video explaining the problem and proposed solution for a general audience.

## Bibliography
* Emerson, H., Guy, M., & McConville, R. (2023). Offline reinforcement learning for safer blood glucose control in people with type 1 diabetes. Journal of Biomedical Informatics, 142, 104376.
* Jinyu Xie. Simglucose v0.2.1 (2018) [Online]. Available: https://github.com/jxx123/simglucose.
* Aguirre-Zapata, E., Cardenas-Cartagena, J., & Garcia-Tirado, J. (2017). Glycemic monitoring in critical care using nonlinear state estimators. IFAC-PapersOnLine, 50(1), 4430-4435.
