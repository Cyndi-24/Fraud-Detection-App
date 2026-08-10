# Fraud Detection Application: Machine Learning Modelling and App Deployment

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

🔗 **Live App:** [https://fraud-detection-app-xm6eiwhsyqcpb4nf553nur.streamlit.app/ ]( MY STREAMLIT_LINK)

## Business Relevance

Fraud detection is not only a technical classification problem; it is also a risk-management and operational decision problem.

A model like this can support banks, fintech companies, payment platforms, e-commerce businesses, and other transaction-based services by helping teams:

- Prioritise suspicious transactions for investigation
- Reduce potential financial losses from fraudulent activity
- Limit unnecessary reviews of legitimate transactions
- Support faster, more consistent transaction-risk screening

The trade-off between precision and recall is especially important in practice. Higher recall helps detect more fraudulent transactions, while higher precision reduces the number of legitimate transactions incorrectly flagged for review.

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

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/evaluation.png)

Random Forest provided the strongest overall balance between fraud precision and recall, making it the most suitable model for the final application.

## Why Random Forest Was Selected

The model comparison showed an important trade-off between detecting as many fraud cases as possible and limiting false fraud alerts.

Logistic Regression achieved 100% fraud recall, meaning it detected every fraudulent transaction in the test set. However, its fraud precision was only 28.9%, indicating a relatively high number of legitimate transactions were also flagged as fraud.

XGBoost improved fraud precision to 40.0% while maintaining 76.9% recall, but its overall balance remained weaker than Random Forest.

Random Forest provided the strongest balance between the two objectives, achieving **70.7% fraud precision, 74.4% fraud recall, and a 72.5% fraud F1-score**. It also produced a ROC-AUC of **0.9996**.

For this reason, Random Forest was selected as the final model for deployment. It provided a more practical balance between identifying fraudulent transactions and reducing unnecessary false alerts.

## Feature Importance & Key Findings

Feature importance analysis showed that **Transaction Value** was the strongest predictor in the Random Forest model, contributing roughly 49% of total feature importance.

Fraudulent transactions also showed a much higher median transaction value than legitimate transactions — approximately **650,000 versus 1,000**. However, the presence of lower-value fraud cases showed that transaction value alone was not enough to classify fraud reliably.

Other predictive signals came from product, provider, transaction timing, category, channel, pricing strategy, and transaction direction. This suggests that fraud detection depended on a combination of transaction characteristics rather than a single rule.

The analysis therefore supports a pattern-based approach to fraud detection, where multiple features are considered together before a transaction is classified.


## Streamlit Application & Deployment

The selected Random Forest model was integrated into an interactive Streamlit application so users can enter transaction details and receive both a fraud classification and estimated fraud probability.

The app was developed and tested in VS Code, connected to the saved model, encoder, scaler, and feature configuration, then deployed through Streamlit using the GitHub repository.

A known fraudulent transaction was used to validate the final deployment, producing a **96% fraud probability** both locally and on the live application.

### Fraudulent Transaction Example

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/fraudulent.png)

### Legitimate Transaction Example

![image alt](https://github.com/Cyndi-24/Fraud-Detection-App/blob/main/Fraud%20detection%20images/legitimate.png)

## Business Recommendations

- Strengthen transaction review around unusually high-value transactions, since fraudulent activity in the dataset was concentrated more heavily among larger transaction amounts.
- Combine transaction value with other patterns such as product type, provider, channel, timing, and transaction direction when deciding which transactions deserve closer attention.
- Focus fraud-monitoring resources on transactions with stronger risk signals rather than treating every transaction with the same level of scrutiny.
- Introduce additional verification for suspicious transactions before completion, especially where the financial exposure is high.
- Review fraud patterns regularly so that transaction controls can be adjusted as customer behaviour, payment channels, and fraud tactics change.

## Limitations & Future Improvements

- This project was developed using a highly imbalanced dataset with only 193 fraudulent transactions, which means model performance is sensitive to a relatively small number of positive cases.

- Transaction Value was the strongest predictor, but the dataset also contained lower-value fraud, so the model should not be interpreted as a simple high-value fraud rule. Its performance may also change when applied to transaction environments with different customer behaviour or fraud patterns.

- Future improvements could include cross-validated hyperparameter tuning, decision-threshold optimisation, additional feature engineering, and validation on new or external transaction data.

## Conclusion

This project demonstrates an end-to-end fraud detection workflow, from data cleaning and feature preparation to model comparison, interpretation, and deployment.Random Forest was selected because it provided the strongest balance between fraud precision and recall among the models tested. The final model was integrated into a Streamlit application that can classify new transactions and return an estimated fraud probability.

Beyond the technical work, the project shows how machine learning can support transaction monitoring, fraud-risk prioritisation, and more informed business decisions.
