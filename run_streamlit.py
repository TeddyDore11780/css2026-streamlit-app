import streamlit as st
import app
import app_plots
import app_profiler
import app_profiler_menus

st.set_page_config(
    page_title="CSS2026 Streamlit App",
    layout="wide",
)

st.title("CSS2026 Dashboard")

menu = st.sidebar.radio(
    "Main Navigation",
    ["Overview", "Plots", "Profiler", "Researcher Menu"],
)

if menu == "Overview":
    app.main()
elif menu == "Plots":
    app_plots.main()
elif menu == "Profiler":
    app_profiler.main()
elif menu == "Researcher Menu":
    app_profiler_menus.main()
