"""

@author: Sonwabile Theodore Mbelebele 208015035
"""
import streamlit as st
import app
import app_plots
import app_profiler

st.set_page_config(
    page_title="CSS2026 Bike App",
    layout="wide"
)

st.title("🚲 CSS2026 Bike Rentals Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Overview", "Plots", "Profiler"]
)

if menu == "Overview":
    app.main()

elif menu == "Plots":
    app_plots.main()

elif menu == "Profiler":
    app_profiler.main()
