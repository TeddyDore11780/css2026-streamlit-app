# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    st.title("Kelly's Space")

    st.write("css_2026_Assignment!")

    st.header("Sample Data")
    data = pd.DataFrame({
        "x": [1, 2, 3],
        "y": [10, 20, 30]
    })
    st.write(data)

    fig = px.line(data, x="x", y="y", title="Simple Plotly Example")
    st.plotly_chart(fig)

    st.header("Bike Data Plot")
    df = pd.read_csv("bike_data.csv")

    # Streamlit native line chart
    st.line_chart(df["n_rented_bikes"])

