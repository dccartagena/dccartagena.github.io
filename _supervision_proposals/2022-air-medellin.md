---
title: "Design of a Deep Learning approach to simulate and forecast smog clouds"
collection: supervision_proposals
permalink: /ideas-projects/2022-air-medellin
date: 2022-12-25
excerpt: This project proposes to develop and evaluate a physics-enhanced deep learning approach for smog cloud modelling by using the growing amount of data on the topic, new deep learning architectures for time-series processing, and the current models as heuristics.
---

## Motivation
Medellin, Colombia, is one of the most polluted places in Latin America due to its growing population, weather, and complex topography. Indeed, pollution has increased respiratory issues in the city’s population[^1]. Medellin is one example of contaminated air, a problem facing several other cities in Latin America, Europe, and the world. For this reason, modelling the smog cloud dynamics may help stakeholders to develop appropriate public health policies and design appropriate control mechanisms for the contamination sources. The existing solution to smog cloud simulation is based on first principle modelling[^2]. Therefore, this project proposes to develop and evaluate a physics-enhanced deep learning approach for smog cloud modelling by using the growing amount of data on the topic, new deep learning architectures for time-series processing, and the current models as heuristics.

<div style="text-align: center;">
    <img src="/images/air_medellin.png"
        alt="Medellin."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>Image is taken from <a href="https://siata.gov.co/sitio_web/index.php/galeria ">siata.gov.co</a></figcaption>
</div>

[^1]:H. Grisales-Romero et al., “Local attributable burden disease to PM2.5 ambient air pollution in Medellín, Colombia, 2010–2016,” F1000Res, vol. 10, p. 428, Dec. 2021, doi: 10.12688/f1000research.52025.2.

[^2]: Daly, A., & Zannetti, P. , “Air pollution modeling–An overview,” Ambient air pollution, 15-28, 2007.

## Tasks and Timeline

### Stage 1:
* Define the estimation problem for smog cloud dynamics;
* Delimitate the solution concept;
* Review the state-of-the-art and proposed solutions in the literature;
* Brainstorm potential deep learning-based solutions for the problem.

### Stage 2:
* Plan the experiments and test for the expected solution;
* Describe the dataset;
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
* Simulation of smog clouds forecasting;
* Mathematical analysis of the proposed algorithm;
* Software with documentation associated with the project;
* Technical report with problem description, proposed solutions, experimental results, and project conclusions by following the University guidelines;
* A public dissertation following the University guidelines.

### Optional Products
* Summary paper from the technical report suitable for conferences or journals;
* 3-minute elevator pitch video of the project;
* Blog post or video explaining the problem and proposed solution for a general audience.

## Bibliography
* P. O’Driscoll, J. Lee, and B. Fu, “Physics Enhanced Artificial Intelligence,” arXiv:1903.04442, Mar. 2019, Accessed: May 09, 2020. Available: http://arxiv.org/abs/1903.04442
* Q. Tao, F. Liu, Y. Li, and D. Sidorov, “Air Pollution Forecasting Using a Deep Learning Model Based on 1D Convnets and Bidirectional GRU,” IEEE Access, vol. 7, pp. 76690–76698, 2019, doi: 10.1109/ACCESS.2019.2921578.