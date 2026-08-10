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
  
  # Methodology

The project followed a structured machine learning workflow:

1. Data Exploration and Cleaning

The dataset was examined to understand its structure, identify missing values, check for null values detect inconsistencies, and prepare the data for analysis through appropriate cleaning and preprocessing techniques.

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/feat_duplicates_missingval.png)

2. Feature Preprocessing
Relevant features were selected and transformed into a suitable format for machine learning. This involved 
encoding categorical variables, scaling numerical features where necessary, and preparing the target variable through the following steps.

* Feature Engineering :This was done to allow the the model to unconver hiding transaction patterns and prevent model overfitting
  
![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature_Engineering.png)

* Feature Encoding:Label encoding was used to convert non-numerical text columns into distinct numerical columns
  
  ![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature_encoding.png)

* Feature Correlation :This was done to ensure to the features strongly relate to each other and the and the target variables

  ![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/correlation_Heatmap.png)
  
* Feature Scaling : This was done to bring the features into the same mathematical range so they can be compareduniformly

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature%20_Scaling.png)
  
3. Train-Test Split

The dataset was divided into training and testing sets to evaluate the model's ability to generalize to unseen data and reduce the risk of overfitting.

4. Model Training
   
A machine learning classification algorithm was trained using the processed training data to learn patterns that distinguish fraudulent transactions from legitimate ones.The following models were used to train the data set;Random Forest Model,XGBoost model and Logistic Regression model

6. Model Evaluation

The trained model was assessed using performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC to measure its effectiveness in detecting fraud.The Random forest model outperformed other models demonstrating superior predictive power.

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature_Model_evaluation.png)

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

