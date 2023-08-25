---
title: "Forecasting building loads, grid carbon intensity and solar generation (based on the Neurips 2023 CityLearn Challenge)"
collection: supervision_proposals
permalink: /ideas-projects/2023-forecasting-loads
date: 2023-08-25
excerpt: This project aims to develop a data preprocessing pipeline and use deep learning models to predict grid quality and resilience in a simulated neighborhood with distributed energy resources.
---

## Motivation

Distributed energy resources (DER) in urban areas, such as solar cells and heat pumps, can help reduce the strain on the power grid during peak hours and increase network resilience, making them a crucial player in mitigating climate change. Proper management is vital to prevent destabilization in the grid and ensure user comfort. For this purpose it is required to develop reliable control systems capable of coordinating each component in the grid. Indeed, model predictive control (MPC) is a suitable technique to boost energy efficiency in the neighbour as it aims to compute a policy by considering a the grid behaviour subject to safety and comfort constraints. However, the fundamental part of MPC is the model itself. Hence, this project aims to develop regression models, based on deep learning techniques, to forecast 48 hours of grid quality and resilience variables in a neighborhood with DER. 

For further information about the challenge, please visit <a href="https://www.aicrowd.com/challenges/neurips-2023-citylearn-challenge/problems/forecasting-track-citylearn-challenge ">AIcrowd - Forecasting Track: CityLearn Challenge</a>

Please note that **the project does not aim to participate in the challenge formally**, but the student is encouraged to use the results in next year’s CityLearn Challenge.

<div style="text-align: center;">
    <img src="/images/linea-transmicion.jpg"
        alt="Linea de transmicion."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption></figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Define the forecasting problem for building loads;
* Delimitate the solution concept within deep learning methods;
* Review the state-of-the-art and proposed solutions in the literature;
* Brainstorm potential deep learning-based solutions for the problem.

### Stage 2:
* Plan the experiments and test for the expected solution;
* Describe the dataset;
* Develop a pre-processing data pipeline;
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
* Simulation of building loads, grid carbon intensity and solar generation;
* Mathematical analysis of the proposed algorithm;
* Software with documentation associated with the project;
* Technical report with problem description, proposed solutions, experimental results, and project conclusions by following the University guidelines;
* A public dissertation following the University guidelines.

### Optional Products
* Summary paper from the technical report suitable for conferences or journals;
* 3-minute elevator pitch video of the project;
* Blog post or video explaining the problem and proposed solution for a general audience.

## Bibliography
* M. Neukomm, V. Nubbe, and R. Fares, “Grid-Interactive Efficient Buildings Technical Report Series: Overview of Research Challenges and Gaps,” NREL/TP-5500-75470, DOE/GO-102019-5227, 1577966, Dec. 2019. doi: 10.2172/1577966.
* T. Brudermüller and M. Kreft, “Smart Meter Data Analytics: Practical Use-Cases and Best Practices of Machine Learning Applications for Energy Data in the Residential Sector,” presented at the ICLR 2023 Workshop: Tackling Climate Change with Machine Learning, Kigali, Rwanda, 2023.
* K. Nweye, A. Wu, H. Park, Y. Almilaify, and Z. Nagy, “CityLearn: A Tutorial on Reinforcement Learning Control for Grid-Interactive Efficient Buildings and Communities,” presented at the ICLR 2023 Workshop: Tackling Climate Change with Machine Learning, Kigali, Rwanda, 2023.


