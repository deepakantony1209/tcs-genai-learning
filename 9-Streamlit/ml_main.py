import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.title("Iris Dataset")
st.write("This is the Iris dataset, which contains measurements of iris flowers from three different species: setosa, versicolor, and virginica.")
st.dataframe(iris)
st.write("The dataset contains the following columns:")
st.write("- sepal_length: The length of the sepal in centimeters.")
st.write("- sepal_width: The width of the sepal in centimeters.")
st.write("- petal_length: The length of the petal in centimeters.")
st.write("- petal_width: The width of the petal in centimeters.")
st.write("- species: The species of the iris flower (setosa, versicolor, or virginica).")
st.write("You can use this dataset to explore the relationships between the different measurements and the species of iris flowers. For example, you can create scatter plots to visualize how sepal length and sepal width vary across the different species, or you can use histograms to examine the distribution of petal lengths for each species.")

@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
data = load_data()
st.write("The dataset has been loaded and cached for faster performance. You can now perform various analyses and visualizations on the data without having to reload it each time.")

## Train model
X = data.drop("species", axis=1)
y = data["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: {accuracy:.2f}")
st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))
st.write("Confusion Matrix:")
st.text(confusion_matrix(y_test, y_pred))

## Inputs for prediction
st.subheader("Make a Prediction")
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.5)
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    st.write(f"The predicted species is: {prediction[0]}")


