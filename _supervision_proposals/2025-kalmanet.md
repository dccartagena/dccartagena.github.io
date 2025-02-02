---
title: "Applications of KalmanNet"
collection: supervision_proposals
permalink: /ideas-projects/2025-kalmanet-applications
date: 2025-01-16
excerpt: We aim to explore and evaluate the capabilities of a hybrid system known as KalmanNet. 
---

## Motivation

The Kalman Filter (KF), proposed by Rudolf E. Kálmán in [1], is one of the most groundbreaking results in signal processing of the 20th century. The filter's key idea is to estimate an unknown variable based on the statistical properties of the variable and observations collected over time. The estimation algorithm is based on the assumptions that there is a linear relationship between the unknown variable and the observations, and that these quantities behave as independent and identically distributed Gaussian random variables. When these assumptions are satisfied, the KF serves as the **optimal** estimator, minimizing the mean squared error between the actual and estimated values of the unknown variable.

One of the main drawbacks of the KF is its reliance on the assumption of a known linear Gaussian **model** in the system. Although it is possible to extend the filter to the non-linear case [2, 3, 4] or apply the same methodology to non-Gaussian variables [5], this assumption remains quite restrictive. In recent decades, there has been a growing emphasis on developing hybrid filters that leverage the theoretical guarantees of the KF with the data-driven flexibility of machine learning models, particularly deep learning approaches [6, 7]. 

Thus, in this project, we aim to explore and evaluate the capabilities of a hybrid system known as KalmanNet, proposed in [8, 9]. This system preserves the model assumption while introducing an adaptive internal architecture based on recurrent neural networks. The evaluation will focus on target applications such as time series estimation with partial information and object tracking. Additionally, we will emphasize explainability, hardware performance, and system accuracy.

<div style="text-align: center;">
    <img src="/images/kalmannet.png"
        alt="Kalman filter block diagram."
        style="display: block; margin-left: auto; margin-right: auto;" />
    <figcaption>Kalman filter block diagram. Image taken from [6]</figcaption>
</div>

## Tasks and Timeline

### Stage 1:
* Literature review on the Kalman Filter and its extensions;
* Reproduce the KalmanNet paper for a simple environment;
* Reproduce well-known extensions of the KF.
* Design a data-driven model to estimate the target variable from the simple environment;
* Select metrics to evaluate performance of each algorithm;
* Benchmark the performance of KalmanNet agains KF, its extensions, and data-driven model.

### Stage 2:
* Choose an application from: 1) Estimation in time series, 2) Object tracking.
* Design data-driven model(s) as baseline.
* Adapt the KF extensions to the application as model-based baselines.
* Select new performance metrics with a focus in explainability, hardware performance, and accuracy.
* Benchmark the proof-of-concept against baselines.

### Stage 3: 
* Document the problem description and experiment-design methodology;
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
[1] R. E. Kalman, “A New Approach to Linear Filtering and Prediction Problems,” Journal of Basic Engineering, vol. 82, no. 1, pp. 35–45, Mar. 1960, doi: 10.1115/1.3662552.

[2] E. A. Wan and R. Van Der Merwe, “The unscented Kalman filter for nonlinear estimation,” in Proceedings of the IEEE 2000 Adaptive Systems for Signal Processing, Communications, and Control Symposium (Cat. No.00EX373), Lake Louise, Alta., Canada: IEEE, 2000, pp. 153–158. doi: 10.1109/ASSPCC.2000.882463.

[3] B. D. Anderson and J. B. Moore, Optimal filtering. in Prentice-Hall information and system sciences series. Englewood Cliffs, N. J.: Prentice-Hall, 1979.

[4] M. Gruber, “An Approach For Target Tracking,” Defense Technical Information Center, Fort Belvoir, VA, Feb. 1967. doi: 10.21236/AD0654272.

[5] N. J. Gordon, D. J. Salmond, and A. F. M. Smith, “Novel approach to nonlinear/non-Gaussian Bayesian state estimation,” IEE Proc. F Radar Signal Process. UK, vol. 140, no. 2, p. 107, 1993, doi: 10.1049/ip-f-2.1993.0015.

[6] S. Feng, X. Li, S. Zhang, Z. Jian, H. Duan, and Z. Wang, “A review: state estimation based on hybrid models of Kalman filter and neural network,” Systems Science & Control Engineering, vol. 11, no. 1, p. 2173682, Dec. 2023, doi: 10.1080/21642583.2023.2173682.

[7] Y. Bai, B. Yan, C. Zhou, T. Su, and X. Jin, “State of art on state estimation: Kalman filter driven by machine learning,” Annual Reviews in Control, vol. 56, p. 100909, 2023, doi: 10.1016/j.arcontrol.2023.100909.

[8] G. Revach, N. Shlezinger, R. J. G. Van Sloun, and Y. C. Eldar, “Kalmannet: Data-Driven Kalman Filtering,” in ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Toronto, ON, Canada: IEEE, Jun. 2021, pp. 3905–3909. doi: 10.1109/ICASSP39728.2021.9413750.

[9] G. Revach, N. Shlezinger, X. Ni, A. L. Escoriza, R. J. G. Van Sloun, and Y. C. Eldar, “KalmanNet: Neural Network Aided Kalman Filtering for Partially Known Dynamics,” IEEE Trans. Signal Process., vol. 70, pp. 1532–1547, 2022, doi: 10.1109/TSP.2022.3158588.







