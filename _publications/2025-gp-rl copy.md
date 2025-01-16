---
title: "Interpretable Function Approximation with Gaussian Processes in Value-Based Model-Free Reinforcement Learning"
collection: publications
permalink: /publication/2025-gp-rl
excerpt: "This paper explores using Gaussian process models in RL for action-value estimation, finding they outperform linear models but lag behind deep neural networks in speed and performance, while offering better uncertainty estimates and interpretability."
date: 2025-12-01
venue: 'Proceedings of the 6th Northern Lights Deep Learning Conference (NLDL)'
paperurl: 'https://proceedings.mlr.press/v265/lende25a.html'
citation: 'Lende, M.v.d., Sabatelli, M. &; Cardenas-Cartagena, J. (2025). Interpretable Function Approximation with Gaussian Processes in Value-Based Model-Free Reinforcement Learning. <i>Proceedings of the 6th Northern Lights Deep Learning Conference (NLDL)</i>, in <i>Proceedings of Machine Learning Research</i> 265:141-154 Available from https://proceedings.mlr.press/v265/lende25a.html.'
---
Estimating value functions in Reinforcement Learning (RL) for continuous spaces is challenging. While traditional function approximators, such as linear models, offer interpretability, they are limited in their complexity. In contrast, deep neural networks can model more complex functions but are less interpretable. Gaussian Process (GP) models bridge this gap by offering interpretable uncertainty estimates while modeling complex nonlinear functions. This work introduces a Bayesian nonparametric framework using GPs, including Sparse Variational (SVGP) and Deep GPs (DGP), for off-policy and on-policy learning. Results on popular classic control environments show that SVGPs/DGPs outperform linear models but converge slower than their neural network counterparts. Nevertheless, they do provide valuable insights when it comes to uncertainty estimation and interpretability for RL. 