Describe a model (maybe fraud mode in capital one, maybe a hypothetical model such as school wants to predict what students will perform better):

1. What method is best? GB, Tree based, logistic Regression, etc.
2. Ask about treatment details.
    - How to treat highly-correlated variables.
    - How to treat outlier.
    - How to treat missing value.
    - Tree model can easily overfit.
3. Main machine learning algorithm methods and pros vs cons.
4. Interpretation of model variables.

In most recent one year, I have done three modeling project, I will give you basic description.


1. Energy consumption prediction (load forecasting) in my previous employer, its a Xgboosting model, the data set is around 80GB, its a 6 month project, I did the prototyping, software architecture design and production code, deployment automation.
2. Online advertisement click rate prediction, its a Kaggle competition. The data set is around 120GB, 250billion rows, its a 2 month teamwork project, and I lead the project and I have two data scientist buddy from Georgetown university, they are now in IBM.
3. Paidoff rate prediction, its a TianChi data scientist competition, tianchi is sponsored by Alipay, it is like chinese kaggle. Its a 1 month project. I did it on my own.




Energy Consumption Prediction
------------------------------------------------------------------------------

**Background**:

One of our core product is Demand Response, it is a system can pre cool your house before the HVAC consumption and the energy price goes high, so it saves you 5%-10% energy bill for Big Office or utility company. In order to do this, a live precise power consumption forecasting is needed.

**About the data**:

- Thermo data: set-point, indoorTemp, load
- Weather data: outdoorTemp, solar power, humidity
- Meta data: house square footage

- Data Source: we have two years of historical data sitting on S3, redshift database, and have a 7 days weather forecasting is available via API.
- Samples: we have millions of data for thousands of individual sensors. The total amount is around 60GB.

**Feature engineering**:

- **Derive more feature**: First it is a time series data, so I derived some running average, running percentile on setpoint, 4Hour, 6Hour, 12Hour lag, it catches unusual setpoint change.
- **Feature encoding**: The hour of day data does mater, so I group hour into 5 morning, noon, afternoon, night, midnight, I use decision tree to maximize the entropy gain. And then do hot encoding.
- **Feature selection**: The shape of outdoorTemp and solar power kind of follow the shape of load, and I use correlation based feature selection select 4Hour, 6Hour, 12Hour lag of setpoint (more important).
- **Missing value**: Missing value, for outdoorTemp, I use linear interpolation.

**Model selection**:

- Auto Regression
- Time Series Regression (Elastic Net)
- Random Forest
- Gradient Boosting (adaboost, xgboost)

**Parameter optimize**:

- general parameter: gbtree
- booster parameter:
    - eta: 0.3, learning rate
    - min_child_weight:
        - XGBoost的这个参数是最小样本权重的和，而GBM参数是最小样本总数。
        - 这个参数用于避免过拟合。当它的值较大时，可以避免模型学习到局部的特殊样本。
        - 但是如果这个值过高，会导致欠拟合。这个参数需要使用CV(GridSearch)来调整。
    - max_depth: 树的最大深度, 如果为3, 说明有8个叶节点
        - 需要用GridSearch来调整.
- objective:
    - objective: reg:linear
    - eval_metric: error cost function

**Result**:

- Use MSE for evaluation.
- **Ercot baseline: 10%, my model: 5%**.
- Ercot prediction range: 7 days, my model: 7 days

**System**:

- Prototyping: sqlite.
- ETL: data call, data engineer, export.
- Trainer: Scheduled worker.
- Predictor: AWS lambda.


Click through rate Prediction
------------------------------------------------------------------------------
Background:

When you surfing on the internet, for example you are reading a tech blog, you may see software advertisement, watching social media like a fashion blogger, you may see cloth, shoes advertisement. The target of this project is: by given page_id, ads_id, and some description data such as document_id, campaign_id, advertiser_id, topic_id, predict that the user gonna click it or not.

The original idea is, me and two of my data scientist friend, we all have solid machine learning experience, but we want to practice our skill on handling big amount of data on limited resource, and want to practice the software development life cycle.

When we start the project, there's a very popular paper about Factorization Machine algorithm, which is proved very powerful on high dimensioned dataset for online advertisement industry. I did the feature engineering by our own.


Paid off rate Prediction
------------------------------------------------------------------------------
**Background**:

Recently in China, IT finance is booming! There's thousands of shopping loan, small loan, consuming loan company. Thanks for the newly built individual credit system.

**About the data**:

This type of loan has terms in 7, 15, 30, and people paid off one times (bullet loan). It doesn't have a english name. And the loan amount is around 300$ to 1000$.

- Start time, end time of the term.
- Paid off time.
- For those people charged off, it has past due day.
- Age, education, gender.

- Samples: 500 data, 60% is paid off, 20% is default, 20% is collection paid off.
- And there's like 10% incomplete data (For default group).

**Data Clean**:

- There's like 10% bad data, specially, the due date doesn't match the paid off days, term doesn't match the start time end time. I remove them.
- There's like 10% incomplete data, the degree, age are missing for some case. For degree, I fill in with college. I supposed to leave it empty, but in practical, the model performs better if I fill it with most common cast college, another reason could be, the college doesn't have significant higher prior probability for paidoff prediction.

**Model**:

At first there's two model comes to my mind: bayesian and KNN, random forest, because:

- all features is category feature, no numeric.
- dataset is not large and not small, complex model such as SVM, Neural network, Xgboost may not work.

Finally I exclude Bayesian and KNN. Because:

- Bayesian rely on data set sampling too much, if I am lucky to choose dominant samples, it works, otherwise its not.
- KNN doesn't have sufficient data, some combination of features doesn't have sufficient samples.
- I finally use **Random forest model** for this, because its more robustic, noise tolerant.

**Feature Engineering**:

- Since I use random forest, I don't have to hot encode category feature. Because it just increase the depth of the tree.
- I derived a very interesting feature, which is the weekday of the paid off date. It gives me 10% increase on accuracy.

**Result**:




