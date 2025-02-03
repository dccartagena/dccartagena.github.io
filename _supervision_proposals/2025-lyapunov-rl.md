---
title: "Lyapunov functions for Safe Reinforcement Learning"
collection: supervision_proposals
permalink: /ideas-projects/2025-lyapunov-safe-rl
date: 2025-01-16
excerpt: TBA
---

## Motivation

One of the pillars of Reinforcement Learning (RL) is trial-and-error

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
* As baseline, design a Q-learning and actor-critic agent to control the target environments. 

### Stage 2:
^ 
* Propose a workflow to learn a Lyapunov function in the target environments;
* Design actor-critic algorithms based on the Lyapunov function;
* Test the algorithms in the target environments;
* Benchmark the proof-of-concept against the baselines solutions.

### Stage 4: 
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
* Wang, J., & Fazlyab, M. (2024). Actor-Critic Physics-informed Neural Lyapunov Control. arXiv preprint arXiv:2403.08448.

* Grüne, L. (2020). Computing Lyapunov functions using deep neural networks. arXiv preprint arXiv:2005.08965.

* Chang, Y. C., Roohi, N., & Gao, S. (2019). Neural lyapunov control. Advances in neural information processing systems, 32.

* Du, D., Han, S., Qi, N., Ammar, H. B., Wang, J., & Pan, W. (2023, May). Reinforcement learning for safe robot control using control lyapunov barrier functions. In 2023 IEEE International Conference on Robotics and Automation (ICRA) (pp. 9442-9448). IEEE.

* Gaby, N., Zhang, F., & Ye, X. (2022, December). Lyapunov-Net: A deep neural network architecture for Lyapunov function approximation. In 2022 IEEE 61st Conference on Decision and Control (CDC) (pp. 2091-2096). IEEE.

