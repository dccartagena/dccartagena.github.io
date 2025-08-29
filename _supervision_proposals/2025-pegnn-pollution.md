---
title: "Scaling Up Physics-Informed GNNs for Air Pollution Forecasting in the Netherlands"
collection: supervision_proposals
permalink: /ideas-projects/2025-pegnn-pollution
date: 2025-08-29
excerpt: This project proposes to build a system based on physics-informed GNN to the problem of multi-pollutant air quality forecasting across the Netherlands.
---

## Motivation

This project proposes leveraging a physics-informed Graph Neural Network (PIGNN) for multi-pollutant air quality forecasting in the Netherlands. By integrating a local advection model, we will guide the GNN's learning process, thereby improving its ability to capture complex spatiotemporal dependencies and generalize across various pollutants. The core objective is to scale an existing single-pollutant forecasting model for the Randstad area into a country-wide system capable of handling multiple pollutants, and then compare its performance against state-of-the-art foundation models for air pollution.

This project is the continuation of [Design of a Deep Learning approach to simulate and forecast smog clouds](/ideas-projects/2022-air-medellin) and [Physics-Enhanced ML for time series forecasting in air pollution](https://dccartagena.github.io/ideas-projects/2025-peml-pollution).

<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Nitrogen_dioxide_over_the_Netherlands_%28TROPOMI%2C_2017-12-01%29.png/960px-Nitrogen_dioxide_over_the_Netherlands_%28TROPOMI%2C_2017-12-01%29.png?20171202110419"
        alt="Nitrogen dioxide over the Netherlands."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>Nitrogen dioxide over the Netherlands. Image is taken from <a href="https://commons.wikimedia.org/wiki/File:Nitrogen_dioxide_over_the_Netherlands_%28TROPOMI,_2017-12-01%29.png">wikimedia.org/...</a></figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Familiarize with the codebase and API of pollution forecasting;
* Review the state-of-the-art for physics enhanced ML in fluid dynamics problems with a focus on GNNs;
* Delimitate the solution concept: We aim to develop a lightweight and trustworthy PIGNN-based system capable of forecasting several air pollutants across the country.

### Stage 2:
* Plan the experiments and tests for the expected solution;
* Adapt the current data and feature pipeline with a focus on scalability;
* Propose relevant metrics related to performance, trustworthiness, and computational resources, to analyse the experiments;
* Implement relevant baselines based on foundation models for air pollution;
* Design a proof-of-concepts of a scalable PIGNN-based system for multi-pollutant forecasting.
* Evaluate the proof-of-concept with the proposed experiments and tests;
* Benchmark the proof-of-concept against other solutions in the literature.

### Stage 3: 
* Document the problem description and solution-design methodology;
* Show the results to reviewers and non-technical audiences.

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
* Assiotis, N., Hau, R., Oldenburg, V., Verbiest, R., Koellermeier, J., Sabatelli, M., and Cardenas-Cartagena, J., "Physics-Informed Graph Neural Networks for Air Pollution Forecasting in the Netherlands" (Accepted at ML-DE @ ECAI 2025. Available under request)
* Oldenburg, V., Cardenas-Cartagena, J., and Valdenegro-Toro, M., “Forecasting Smog Clouds With Deep Learning”, <i>arXiv e-prints</i>, Art. no. arXiv:2410.02759, 2024. doi:10.48550/arXiv.2410.02759.
* P. O’Driscoll, J. Lee, and B. Fu, “Physics Enhanced Artificial Intelligence,” arXiv:1903.04442, Mar. 2019, Accessed: May 09, 2020. Available: http://arxiv.org/abs/1903.04442
* Q. Tao, F. Liu, Y. Li, and D. Sidorov, “Air Pollution Forecasting Using a Deep Learning Model Based on 1D Convnets and Bidirectional GRU,” IEEE Access, vol. 7, pp. 76690–76698, 2019, doi: 10.1109/ACCESS.2019.2921578.
* Bodnar, C., Bruinsma, W. P., Lucic, A., Stanley, M., Allen, A., Brandstetter, J., ... & Perdikaris, P. (2025). A foundation model for the Earth system. Nature, 1-8.
