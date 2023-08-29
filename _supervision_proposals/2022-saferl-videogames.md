---
title: "Implementation of Safe Deep Learning algorithms in videogames"
collection: supervision_proposals
permalink: /ideas-projects/2022-saferl-videogames
date: 2022-12-24
excerpt: This project aims to benchmark safe RL and propose novel ideas to improve the existing state-of-the-art in the area.
---

## Motivation
Safe Reinforcement Learning (safe RL) is a branch of data-driven control and machine learning whose main focus is guaranteeing a safe operation in a system while optimizing some efficiency criteria. Although there are exciting advances in this topic, the algorithms are not mature enough to implement in real-life scenarios such as offshores or wind farms. Thus, it still requires more development and testing in complex but harmless environments such as video games. Therefore, this project aims to benchmark safe RL and propose novel ideas to improve the existing state-of-the-art in the area. There are two target environments: Super Mario and Minecraft, but it is possible to consider other video games. Those environments suppose a multitasking challenge for the safe RL agent while keeping safe behaviour in the game.

<div style="text-align: center;">
    <img src="/images/super-mario.jpg"
        alt="Mario."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>Image is taken from <a href="https://www.hippopx.com/en/query?q=video%20Game">hippopx.com</a></figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Define the safe reinforcement learning problem in video games;
* Delimitate the solution concept;
* Review the state-of-the-art and proposed solutions in the literature;
* Brainstorm potential solutions for the problem.

### Stage 2:
* Plan the experiments and test for the expected solution;
* Set up a suitable video game environment for experimentation;
* Collect data from the environment;
* Develop a pre-processing data methodology;
* Select meaningful features from the dataset;
* Design a proof-of-concept for potential solutions via minimum viable product concept;
* Analyze the proposed proof-of-concept.

### Stage 3: 
* Evaluate the proof-of-concept with the proposed experiments and tests;
* Benchmark the proof-of-concept against other solutions in the literature.

### Stage 4: 
* Document the problem description and solution-design methodology;
* Show the results to reviewers and non-technical audiences.

## Expected Outcomes

### Mandatory Products
* An autonomous agent capable of playing video games by considering safety constraints;
* Benchmark with other (safe) reinforcement learning algorithms in the literature;
* Mathematical analysis of the proposed algorithm;
* Software with documentation associated with the project;
* Technical report with problem description, proposed solutions, experimental results, and project conclusions by following the University guidelines;
* A public dissertation following the University guidelines.


### Optional Products
* Summary paper from the technical report suitable for conferences or journals;
* 3-minute elevator pitch video of the project;
* Blog post or video explaining the problem and proposed solution for a general audience.

## Bibliography
* J. Garcıa and F. Fernández, “A comprehensive survey on safe reinforcement learning,” Journal of Machine Learning Research, vol. 16, no. 1, Art. no. 1, 2015.
* A. Hans, D. Schneegaß, A. M. Schafer, and S. Udluft, “Safe Exploration for Reinforcement Learning,” Artificial Neural Networks, p. 6, 2008.
* M. Heger, “Consideration of Risk in Reinforcement Learning,” in Machine Learning Proceedings 1994, Elsevier, 1994, pp. 105–111. doi: 10.1016/B978-1-55860-335-6.50021-0.
* W. Saunders, G. Sastry, A. Stuhlmueller, and O. Evans, “Trial without Error: Towards Safe Reinforcement Learning via Human Intervention,” Proc. Int. Jt. Conf. Auton. Agents Multiagent Syst. AAMAS, vol. 3, pp. 2067–2069, Jul. 2017.