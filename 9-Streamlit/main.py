import streamlit as st
import pandas as pd
import numpy as np


# Streamlit app to demonstrate its capabilities
# This app will display a welcome message and some basic information about Streamlit.

# Set the title of the app
st.title("Welcome to Streamlit!")

# Display a header
st.header("What is Streamlit?")

# Display some text about Streamlit
st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps - so let's get started!")

# Display a subheader
st.subheader("Key Features of Streamlit")

# List some key features of Streamlit
features = [
    "Easy to use: Streamlit's API is simple and intuitive, allowing you to create interactive apps with just a few lines of code.",
    "Fast development: Streamlit's hot-reloading feature allows you to see changes in real-time as you edit your code.",
    "Customizable: Streamlit provides a wide range of widgets and components that you can use to customize your app's appearance and functionality.",
    "Integration: Streamlit can easily integrate with popular Python libraries like NumPy, Pandas, Matplotlib, and more.",
    "Deployment: Streamlit apps can be deployed easily on platforms like Streamlit Cloud, Heroku, or any cloud service that supports Python."
]

for feature in features:
    st.write(f"- {feature}")

# Display a success message
st.success("Streamlit makes it easy to create and share data apps. Give it a try and see how it can enhance your data science projects!")

# Markdown for additional information
st.markdown("""
### Learn More
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)
- [Streamlit Community Forum](https://discuss.streamlit.io/)
""")

# Caption
st.caption("This is a simple Streamlit app to demonstrate its features. You can customize it further by adding more widgets, charts, and interactivity!")

# Dispalying dataframe

data = pd.DataFrame({
    'Column A': np.random.rand(10),
    'Column B': np.random.rand(10),
    'Column C': np.random.rand(10)
})
st.subheader("Example DataFrame")
st.subheader("Using st.dataframe")
st.write("The st.dataframe function allows you to display a DataFrame with interactive features like sorting and filtering.")
st.dataframe(data)

st.subheader("Using st.table")
st.write("The st.table function displays a static table without interactive features.")
st.table(data)

## Widgets
st.subheader("Widgets")
st.write("Streamlit provides a variety of widgets to create interactive apps. Here are some examples:")

# Text input widget
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
# Slider widget
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")
# Number input widget
number = st.number_input("Enter a mark:", min_value=0, max_value=100, value=50)
st.write(f"You entered a mark of {number}.")
# Slider widget for selecting a range
range_values = st.slider("Select a range of values:", 0, 100, (60, 80))
st.write(f"You selected the range: {range_values}")

## Selectbox widget
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

## Checkbox widget
if st.checkbox("Show more information"):
    st.write("Here is some additional information that is displayed when the checkbox is checked.")

## Radio button widget
radio_option = st.radio("Choose a radio option:", ["Radio 1", "Radio 2", "Radio 3"])
st.write(f"You selected: {radio_option}")

# Button widget
if st.button("Click me"):
    st.write("Button clicked! You can perform any action you want when the button is clicked.")

## Layouts and containers

## Sidebar
st.sidebar.header("Sidebar")
sidebar_option = st.sidebar.selectbox("Choose a sidebar option:", ["Sidebar Option 1", "Sidebar Option 2", "Sidebar Option 3"])
st.sidebar.write(f"You selected: {sidebar_option}")

## Columns
st.subheader("Columns")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")
with col3:
    st.write("This is column 3")

## Expander
st.subheader("Expander")
with st.expander("Click to expand"):
    st.write("This content is hidden inside an expander. Click the expander to reveal this content.")

## File upload
st.subheader("File Upload")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size} bytes")

## Progress bar
import time
st.subheader("Progress Bar")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

## Forms
st.subheader("Forms")
with st.form("my_form"):
    st.write("This is a form. You can add multiple input widgets inside this form.")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write(f"Form submitted! Name: {name}, Age: {age}")

## Charts
st.subheader("Charts")
chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

## Maps
st.subheader("Maps")
map_data = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

## Cache
@st.cache
def expensive_computation(num):
    time.sleep(2)  # Simulate a time-consuming computation
    return num * num

st.subheader("Caching")
number = st.number_input("Enter a number for expensive computation:", value=10)
result = expensive_computation(number)
st.write(f"The result of the expensive computation is: {result}")