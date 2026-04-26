import tensorflow as tf
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

# Load the model
model = tf.keras.models.load_model('models/model.h5')

# Load the encoders
with open('models/ordinal_encoder.pkl', 'rb') as f:
    ordinal_encoder = pickle.load(f)

with open('models/one_hot_encoder.pkl', 'rb') as f:
    onehot_encoder = pickle.load(f)

with open('models/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

with open('models/standard_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


## Streamlit app
import streamlit as st
st.title("Customer Churn Prediction")

# Input fields
geography = st.selectbox('Geography', onehot_encoder.categories_[0])
gender = st.selectbox('Gender', label_encoder.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
complain = st.selectbox('Complain', [0, 1])
satisfaction_score = st.slider('Satisfaction Score', 1, 5)
card_type = st.selectbox('Card Type', ['SILVER', 'GOLD', 'PLATINUM'])
point_earned = st.number_input('Point Earned')

input_data = {
    'CreditScore':[credit_score],
    'Geography':[geography],
    'Gender':[gender],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary],
    'Complain':[complain],
    'Satisfaction Score':[satisfaction_score],
    'Card Type':[card_type],
    'Point Earned':[point_earned]
}

# Preprocess input data
input_df = pd.DataFrame(input_data)
input_df['Card Type'] = ordinal_encoder.transform(input_df[['Card Type']])
input_df['Gender'] = label_encoder.transform(input_df['Gender'])
geography_encoded = onehot_encoder.transform(input_df[['Geography']]).toarray()
geography_df = pd.DataFrame(geography_encoded, columns=onehot_encoder.get_feature_names_out(['Geography']))
input_df = input_df.drop('Geography', axis=1)
input_df = pd.concat([input_df, geography_df], axis=1)
input_df_scaled = scaler.transform(input_df)


# Make prediction
prediction = model.predict(input_df_scaled)
predicted_churn = (prediction > 0.5).astype(int)
if st.button('Predict Churn'):
    if predicted_churn[0][0] == 1:
        st.write(f'Predicted Churn Probability: {prediction[0][0]}')
        st.error('The customer is likely to churn.')
    else:
        st.write(f'Predicted Churn Probability: {prediction[0][0]}')
        st.success('The customer is unlikely to churn.')