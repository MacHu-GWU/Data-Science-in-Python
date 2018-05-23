Missing Value (缺失值)
==============================================================================
在数据清洗过程中, 我们经常会遇到缺失值问题.


Analyze Importance.
------------------------------------------------------------------------------
1. **Not important, and not required**: Ignore it.
2. **Not important, but required**: fill in interpolated value, average value, median value or we build a value.
3. **Important**: I prefer to build a model to estimate the value, for example: for numeric value, a Nearest Neighbor Regression, a Linear Regression model; for labeled value: a Bayesian model, decision tree model ...
4. How many? missing > 80%, ignore it, < 50% fill in a fix value, between 50% to 80%, build model for it.


Does the model sensitive to missing value?
------------------------------------------------------------------------------
1. Regression: Sensitive.
2. Decision Tree Model: NOT sensitive.
