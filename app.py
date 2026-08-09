import streamlit as st
import pandas as pd
import pickle
from scipy.sparse import hstack
# Load corrected model and preprocessing objects
with open("fraud_model_fixed.pkl", "rb") as file:
    model = pickle.load(file)

with open("fraud_encoder_fixed.pkl", "rb") as file:
    encoder = pickle.load(file)

with open("fraud_scaler_fixed.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("fraud_feature_info_fixed.pkl", "rb") as file:
    feature_info = pickle.load(file)

categorical_cols = feature_info["categorical_cols"]
numerical_cols = feature_info["numerical_cols"]

st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="🔍",
    layout="centered"
)
st.title("Fraud Detection App")

st.write(
    "Use the transaction details in the sidebar to assess whether a transaction "
    "is likely to be fraudulent."
)


with st.sidebar:
    st.header("Transaction Details")

    provider_id = st.selectbox(
        "Provider ID",
        ["ProviderId_1", "ProviderId_2", "ProviderId_3",
         "ProviderId_4", "ProviderId_5", "ProviderId_6"]
    )

    product_id = st.selectbox(
        "Product ID",
        [f"ProductId_{i}" for i in range(1, 28)]
    )

    product_category = st.selectbox(
        "Product Category",
        [
            "airtime",
            "financial_services",
            "utility_bill",
            "data_bundles",
            "tv",
            "transport",
            "ticket",
            "movies",
            "other"
        ]
    )

    channel_id = st.selectbox(
        "Channel ID",
        ["ChannelId_1", "ChannelId_2", "ChannelId_3", "ChannelId_5"]
    )

    value = st.number_input(
        "Transaction Value",
        min_value=0.0,
        value=1000.0
    )

    pricing_strategy = st.selectbox(
        "Pricing Strategy",
        [0, 1, 2, 4]
    )

    month = st.slider(
        "Transaction Month",
        1, 12, 1
    )

    day = st.slider(
        "Transaction Day",
        1, 31, 1
    )

    credit_or_debit = st.selectbox(
        "Credit or Debit",
        [0, 1],
        format_func=lambda x: "Credit" if x == 0 else "Debit"
    )
    

if st.button("Predict Fraud"):

    input_data = {
        "ProviderId": provider_id,
        "ProductId": product_id,
        "ProductCategory": product_category,
        "ChannelId": channel_id,
        "Value": value,
        "PricingStrategy": pricing_strategy,
        "Month": month,
        "Day": day,
        "credit_or_debit": credit_or_debit
    }

    input_df = pd.DataFrame([input_data])

    input_cat = input_df[categorical_cols].astype(str)
    input_num = input_df[numerical_cols]

    input_cat_encoded = encoder.transform(input_cat)
    input_num_scaled = scaler.transform(input_num)

    input_processed = hstack([
        input_num_scaled,
        input_cat_encoded
    ])

    prediction = model.predict(input_processed)[0]
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("This transaction is predicted to be fraudulent.")
    else:
        st.success("This transaction is predicted to be legitimate.")