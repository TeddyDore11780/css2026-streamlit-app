# -*- coding: utf-8 -*-
"""


@author: Sonwabile Theodore Mbelebele 208015035
"""

import streamlit as st
import pandas as pd

def main():
    st.title("Title heading")

    st.write("Hello, Streamlit!")
    st.write("Hello2")

    st.header("Overview")
    df = pd.read_csv("bike_data.csv")
    st.dataframe(df.head())

    st.header("Number selection")
    number = st.slider("Pick a number", 1, 100)
    st.write(f"You picked: {number}")
