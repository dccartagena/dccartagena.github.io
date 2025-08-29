---
title: "Scaling Up Physics-Informed GNNs for Air Pollution Forecasting in the Netherlands"
collection: supervision_proposals
permalink: /ideas-projects/2025-pegnn-pollution
date: 2025-08-29
excerpt: This project proposes to build a system based on physics-informed GNN to the problem of multi-pollutant air quality forecasting across the Netherlands.
---

## Motivation

This project proposes leveraging a physics-informed Graph Neural Network (GNN) for multi-pollutant air quality forecasting in the Netherlands. By integrating a local advection model, we will guide the GNN's learning process, thereby improving its ability to capture complex spatiotemporal dependencies and generalize across various pollutants. The core objective is to scale an existing single-pollutant forecasting model for the Randstad area into a country-wide system capable of handling multiple pollutants, and then compare its performance against state-of-the-art foundation models for air pollution.

This project is the continuation of [Design of a Deep Learning approach to simulate and forecast smog clouds](/ideas-projects/2022-air-medellin) and [Physics-Enhanced ML for time series forecasting in air pollution](https://dccartagena.github.io/ideas-projects/2025-peml-pollution).

<div style="text-align: center;">
    <img src="/images/pollution.jpg"
        alt="Linea de transmicion."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption><a href="https://commons.wikimedia.org/wiki/File:IJmuiden,_the_Netherlands_(9043390013).jpg">Ineke Huizing from Alphen aan den Rijn, the Netherlands</a>, <a href="https://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>, via Wikimedia Commons</figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Familiarize with the codebase and API of pollution forecasting;
* Review the state-of-the-art for physics enhanced ML in fluid dynamics problems with a focus on GNNs;
* ...

### Stage 2:
* Plan the experiments and tests for the expected solution;
* ...
* 
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
