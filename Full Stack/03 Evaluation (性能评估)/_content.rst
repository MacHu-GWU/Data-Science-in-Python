Evaluation (性能评估)
==============================================================================
在建立一个模型之后, 评估一个模型的好坏, 我们往往有下面这些标准.

- 2 Class:
    - ROC, AUC
    - PRC
- N class:
    - Confusion Matrix:
    - Accuracy Score:
    - Logloss: 2 - N Class	Output is probability instead of label, Usually for Logistic Regression, because the cost function is similar to maxlikelyhood function
- Regression:
    - Mean Absolute Error (MAE)
    - Mean Square Error (MSE)
    - Median Absolute Error
- Clustering:
    - **Calinski-Harabaz Index**: Use this when you don't know the actual label. For covariance, **within-cluster the smaller the better, between-cluster is opposite**
