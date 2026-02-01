# -*- coding: utf-8 -*-
"""


@author: Sonwabile Theodore Mbelebele 208015035
"""

import streamlit as st
import pandas as pd

def main():
    st.title("2026 Coding Summer school Assignment")

    st.write("Hello, Streamlit!")
    st.write("Welcome To Kelly's Space")

    st.header("Overview")
    df = pd.read_csv("bike_data.csv")
    st.dataframe(df.head())

    st.header("Number selection")
    number = st.slider("Pick a number", 1, 100)
    st.write(f"You picked: {number}")

