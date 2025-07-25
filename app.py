import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Data Visualization App", layout="wide")
st.title("Sample data visualization app")
st.sidebar.header("Settings")
st.sidebar.subheader("Data Generation Settings")
num_rows = st.sidebar.slider("Number of rows", 100, 1000, 500)
st.sidebar.subheader("Chart Settings")
chart_type = st.sidebar.selectbox(
    "Select chart type", ["Line Chart", "Bar Chart", "Scatter Plot"]
)


@st.cache_data
def generate_data(num_rows: int) -> pd.DataFrame:
    np.random.seed(42)
    dates = pd.date_range(start="2020-01-01", periods=num_rows, freq="D")
    data = {
        "Date": dates,
        "Value1": np.random.rand(num_rows) * 100,
        "Value2": np.random.rand(num_rows) * 100,
    }
    return pd.DataFrame(data)


data = generate_data(num_rows)

st.subheader("Generated Data")
st.dataframe(data)

if chart_type == "Line Chart":
    fig = px.line(data, x="Date", y=["Value1", "Value2"], title="Line Chart of Values")
elif chart_type == "Bar Chart":
    fig = px.bar(data, x="Date", y=["Value1", "Value2"], title="Bar Chart of Values")
elif chart_type == "Scatter Plot":
    fig = px.scatter(
        data, x="Value1", y="Value2", color="Date", title="Scatter Plot of Values"
    )

st.plotly_chart(fig)
