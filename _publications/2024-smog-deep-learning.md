---
title: "Forecasting Smog Clouds With Deep Learning: A Proof-Of-Concept"
collection: publications
permalink: /publication/2024-smog-deep-learning
excerpt: "This study investigates deep learning models, particularly LSTMs and GRUs, for multi-location air pollution forecasting of NO2, O3, PM10 & PM2.5, with a hierarchical GRU emerging as the most effective method."
date: 2024-07-24
venue: 'ICML 2024, AI4Science'
paperurl: 'https://openreview.net/forum?id=UQa2PEVHMF&nesting=2&sort=date-desc'
citation: 'Oldenburg, V., Cardenas-Cartagena, J., & Valdenegro-Toro, M. (2024). Forecasting Smog Clouds With Deep Learning. arXiv preprint arXiv:2410.02759.'
---
In this proof-of-concept study, we conduct multivariate timeseries forecasting for the concentrations of nitrogen dioxide (NO2), ozone (O3), and (fine) particulate matter (PM10 & PM2.5) with meteorological covariates between two locations using various deep learning models, with a focus on long short-term memory (LSTM) and gated recurrent unit (GRU) architectures. In particular, we propose an integrated, hierarchical model architecture inspired by air pollution dynamics and atmospheric science that employs multi-task learning and is benchmarked by unidirectional and fully-connected models. Results demonstrate that, above all, the hierarchical GRU proves itself as a competitive and efficient method for forecasting the concentration of smog-related pollutants.