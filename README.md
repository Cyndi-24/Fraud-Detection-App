# Fraud Detection Application: Full Cycle Machine Learning Modelling and App Deployment

__________________

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Fraud_Detection_image.png)

_________________

## Project Overview

This project develops an end-to-end machine learning solution for identifying potentially fraudulent financial transactions. It covers transaction data preparation, exploratory analysis, feature engineering, model development and comparison, model interpretation, and deployment through an interactive Streamlit application.

A key challenge was the severe class imbalance in the dataset, where fraudulent transactions represented only a small proportion of all transactions. For this reason, model evaluation focused on fraud-class precision, recall, F1-score, confusion matrix, and ROC-AUC rather than relying on accuracy alone.

Three classification models — Logistic Regression, XGBoost, and Random Forest — were evaluated before selecting the final model for deployment.

## Project Objective

The objective of this project was to develop and evaluate a machine learning model capable of identifying potentially fraudulent transactions while maintaining a useful balance between detecting fraud and limiting false alerts.

The project also aimed to understand the transaction characteristics associated with fraud and translate the final predictive model into an interactive application that can evaluate new transaction inputs.

## Analytical Questions

1. Can transaction characteristics be used to distinguish fraudulent transactions from legitimate transactions?
2. Which transaction characteristics contribute most strongly to fraud prediction?
3. How do fraudulent transactions differ from legitimate transactions?
4. Which classification model provides the most balanced performance for detecting the minority fraud class?
5. Can the selected model be deployed through an interactive application for screening new transactions

## Tools Used

- **Python** — data preparation, feature engineering, model development, and evaluation
- **Pandas & NumPy** — data manipulation and analysis
- **Scikit-learn** — preprocessing, Logistic Regression, Random Forest, and model evaluation
- **XGBoost** — gradient-boosted classification model
- **Matplotlib & Seaborn** — exploratory analysis and visualisation
- **Jupyter Notebook** — analysis and model development
- **VS Code** — Streamlit application development and testing
- **Streamlit** — interactive fraud prediction application
- **GitHub** — project documentation, version control, and deployment repository

## Approach

1. Cleaned and prepared the transaction data, removed non-predictive identifiers, and engineered time and transaction-direction features.
2. Split the data into training and test sets before fitting preprocessing objects to reduce data leakage.
3. One-hot encoded categorical variables and scaled numerical variables.
4. Addressed the severe class imbalance and evaluated Logistic Regression, XGBoost, and Random Forest using fraud-class precision, recall, F1-score, confusion matrix, and ROC-AUC.
5. Compared model performance, interpreted feature importance, and investigated the transaction patterns associated with fraud.
6. Selected the best-performing model, saved the required preprocessing objects, and deployed the final solution through Streamlit.
   
## Data Cleaning & Preparation

Before modelling, the transaction dataset was inspected and prepared to ensure that the features used for training were consistent and analysis-ready.

Key preparation steps included:

- Checked the dataset for missing values and duplicate records.
- Reviewed column data types and corrected fields that required appropriate numeric, categorical, or datetime treatment.
- Converted transaction timestamps to datetime format and extracted **Month** and **Day** as additional time-based features.
- Derived a **credit/debit indicator** from transaction direction.
- Reviewed categorical fields such as Provider ID, Product ID, Product Category, and Channel ID before encoding.
- Removed identifier and non-predictive fields from the modelling dataset while retaining them where useful for transaction traceability.
- Verified the cleaned feature set before splitting the data for model training and evaluation.

## Dataset & Class Imbalance

The dataset contains 95,662 financial transactions, of which only 193 were labelled as fraudulent. This means fraud represented roughly 0.2% of all transactions, creating a severe class-imbalance problem.

Because overall accuracy can appear very high even when a model fails to detect fraud, evaluation focused on the minority fraud class using precision, recall, F1-score, confusion matrix, and ROC-AUC.

To address the imbalance, model-specific class weighting was used instead of synthetic oversampling:

- `class_weight="balanced"` for Logistic Regression and Random Forest
- `scale_pos_weight` for XGBoost, calculated from the ratio of legitimate to fraudulent transactions

Class weighting was preferred over SMOTE because it increases the penalty for misclassifying rare fraud cases without creating synthetic transactions. This kept the training data closer to the original transaction distribution, reduced the risk of introducing unrealistic fraud patterns, and kept the preprocessing pipeline simpler.

## Feature Preparation

Once the data was cleaned, the next step was to prepare it for modelling.

Identifier fields such as Transaction ID, Batch ID, Account ID, Subscription ID, and Customer ID were excluded from the predictive feature set because they mainly identify individual records and could encourage the model to memorise transactions rather than learn meaningful fraud patterns.

The remaining variables were grouped into categorical and numerical features. Provider ID, Product ID, Product Category, and Channel ID were one-hot encoded, while numerical features such as transaction value, pricing strategy, month, day, and the credit/debit indicator were scaled.

To avoid data leakage, the train-test split was completed before fitting the encoder and scaler. The preprocessing steps were learned from the training data and then applied to the test data.

## Models Evaluated

Three classification models were tested to compare how well different approaches could identify the minority fraud class:

- **Logistic Regression** — used as a baseline model with class weighting to give greater importance to fraudulent transactions.
- **XGBoost** — used to capture more complex non-linear relationships, with `scale_pos_weight` applied to account for the severe class imbalance.
- **Random Forest** — used as an ensemble tree-based model with balanced class weights to improve sensitivity to fraud cases.

The models were compared using precision, recall, F1-score, confusion matrix, ROC-AUC, and overall classification behaviour, with particular attention given to performance on fraudulent transactions rather than overall accuracy alone.


## Model Comparison & Results

The three models were compared with particular attention to their ability to identify fraudulent transactions rather than overall accuracy alone.

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/evaluation.png

Random Forest provided the strongest overall balance between fraud precision and recall, making it the most suitable model for the final application.



6. Application Deployment
The serialized model was integrated into an interactive web application, enabling users to input transaction details and receive real-time fraud predictions through an intuitive interface.

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/fraud_app.png)

# Features
* Predicts fraudulent transactions in real time
* User-friendly interface
* Instant prediction results
* Supports decision-making for fraud screening
* Demonstrates practical application of machine learning

# Business Value
Fraud detection systems help organizations:
* Reduce financial losses
* Detect suspicious transactions early
* Improve operational efficiency
* Support risk management
* Enhance customer trust

# Limitations
* The model was trained on a specific dataset and may not generalize well to all real-world transaction patterns.
* Fraudulent transactions are typically much less frequent than legitimate ones, which can introduce class imbalance and affect prediction performance.
* Predictions are based solely on the features available in the dataset and do not incorporate external or real-time transaction data.
* The application is intended for educational and portfolio purposes and should not be used as a production fraud detection system without further validation and testing.

