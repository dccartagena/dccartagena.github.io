---
title: "Lyapunov functions for Safe Deep Reinforcement Learning"
collection: supervision_proposals
permalink: /ideas-projects/2025-lyapunov-safe-rl
date: 2025-01-16
excerpt: In this project, we aim to learn Lyapunov functions using DNNs and leverage them to guide the training of actor-critic agents toward safe behavior.
---

## Motivation

Deep Reinforcement Learning (DRL) has demonstrated outstanding empirical performance in nonlinear control tasks within high-dimensional environments, primarily in digital settings where mistakes are inexpensive and harmless. However, transitioning from these digital environments to cyber-physical systems requires safety performance guarantees.

Integrating concepts from control theory in RL can enhance the safe behavior of the control agent, particularly through Lyapunov functions, which provide theoretical safety guarantees in stability tasks, such as the inverted pendulum environment. In simple environments, a Lyapunov function can be manually designed as a quadratic function of state and control variables. However, in more complex environments, it can be approximated as the solution of a partial differential equation (PDE) using deep neural networks (DNNs) [1, 2]. Thus, in this project, we aim to learn Lyapunov functions using deep neural networks and leverage them to guide the training of actor-critic agents toward safe behavior.

<div style="text-align: center;">
    <img src="/images/robot-balancing.png"
        alt="Robot Balancing."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>Robot Balancing. Image generated with Dall-e</figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Review the state-of-the-art on Lyapunov functions and RL;
* Implement a Linear-Quadratic-Controller (LQR) on the Gymnasium's control environments;
* As baseline, compute stability guarantees for the LQR based on associated Lyapunov function; 
* As baseline, design a Deep Q-learning and Actor-Critic agent to control the target environments. 

### Stage 2:
* Propose a workflow to learn a Lyapunov function in the target environments;
* Design actor-critic algorithms based on the Lyapunov function;
* Compute safety guarantees for the algorithm based on safe regions coming from the Lyapunov functions;
* Test the algorithms in the target environments;
* Benchmark the proof-of-concept against the baselines solutions.

### Stage 3: 
* Document the problem description and solution-design methodology;
* Show the results to reviewers and non-technical audiences.

## Expected Outcomes

### Mandatory Products
* Mathematical analysis of the proposed algorithms;
* Software with documentation associated with the project;
* Technical report with problem description, proposed solutions, experimental results, and project conclusions by following the University guidelines;
* A public dissertation following the University guidelines.

### Optional Products
* Summary paper from the technical report suitable for conferences or journals;
* 3-minute elevator pitch video of the project;
* Blog post or video explaining the problem and proposed solution for a general audience.

## Bibliography
[1] Wang, J., & Fazlyab, M. (2024). Actor-Critic Physics-informed Neural Lyapunov Control. arXiv preprint arXiv:2403.08448.

[2] Grüne, L. (2020). Computing Lyapunov functions using deep neural networks. arXiv preprint arXiv:2005.08965.

* Chang, Y. C., Roohi, N., & Gao, S. (2019). Neural lyapunov control. Advances in neural information processing systems, 32.

* Du, D., Han, S., Qi, N., Ammar, H. B., Wang, J., & Pan, W. (2023, May). Reinforcement learning for safe robot control using control lyapunov barrier functions. In 2023 IEEE International Conference on Robotics and Automation (ICRA) (pp. 9442-9448). IEEE.

* Gaby, N., Zhang, F., & Ye, X. (2022, December). Lyapunov-Net: A deep neural network architecture for Lyapunov function approximation. In 2022 IEEE 61st Conference on Decision and Control (CDC) (pp. 2091-2096). IEEE.

