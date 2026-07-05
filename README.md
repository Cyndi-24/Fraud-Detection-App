# Fraud Detection : Full Cycle Machine Learning Modelling and App Deployment
## By Ofolebe Cyndi

__________________
![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Fraud_Detection_image.png)


_________________

# Project Overview
Financial fraud is a growing challenge for banks and payment providers, resulting in billions of dollars in losses each year. This project demonstrates how machine
learning can be used to identify potentially fraudulent transactions and support faster, data-driven decision-making.
This project embodies an end to end machine learning pipeline and deployed streamlit application  which predicts whether a transaction is Fraudulent or Legitimate based on transaction characteristics provided by the user.

# Project Objectives
* Develop a machine learning model capable of detecting fraudulent transactions. 
* Build an interactive application for real-time fraud prediction.
* Demonstrate an end-to-end data science workflow from data preprocessing to deployment.
* Showcase how predictive analytics can support fraud prevention.

# Dataset
The dataset captures financial transactions originating from Uganda utilizing Ugandan Shilings (UGX) as the baseline currency.It includes features representing transaction behavior and a target variable indicating whether a transaction was fraudulent.

# Technologies Used
* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit (or Flask, depending on your app)
* Git & GitHub

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
  
* feature Scaling : This was done to bring the features into the same mathematical range so they can be compareduniformly

![image alt] (https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature%20_Scaling.png)
  
3. Train-Test Split

The dataset was divided into training and testing sets to evaluate the model's ability to generalize to unseen data and reduce the risk of overfitting.

4. Model Training
A machine learning classification algorithm was trained using the processed training data to learn patterns that distinguish fraudulent transactions from legitimate ones.The following models were used to train the data set;Random Forest Model,XGBoost model and Logistic Regression model

5. Model Evaluation

The trained model was assessed using performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC to measure its effectiveness in detecting fraud.The Random forest model outperformed other models demonstrating superior predictive power.

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/Feature_Model_evaluation.png)

6. Application Deployment

The serialized model was integrated into an interactive web application, enabling users to input transaction details and receive real-time fraud predictions through an intuitive interface.

![image alt](

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

