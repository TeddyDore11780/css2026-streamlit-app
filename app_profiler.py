import streamlit as st
import pandas as pd
import numpy as np


def main():
    # Title of the app
    st.title("Researcher Profile Page with STEM Data")

    # Profile Section
    st.header("Researcher Overview")
    name = "Dr. Jane Doe"
    field = "Astrophysics"
    institution = "University of Science"

    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.image(
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
        caption="Nature (Pixabay)"
    )

    # Publications Section
    st.header("Publications")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)

    # Publication Trends
    st.header("Publication Trends")
    if uploaded_file and "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    elif uploaded_file:
        st.info("No 'Year' column found for trend visualization.")

    # STEM Data Section
    st.header("Explore STEM Data")

    physics_data = pd.DataFrame({
        "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
        "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
        "Date": pd.date_range(start="2024-01-01", periods=5),
    })

    astronomy_data = pd.DataFrame({
        "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
        "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
        "Observation Date": pd.date_range(start="2024-01-01", periods=5),
    })

    weather_data = pd.DataFrame({
        "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
        "Temperature (°C)": [25, 10, -3, 15, 30],
        "Humidity (%)": [65, 70, 55, 80, 50],
        "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
    })

    st.subheader("STEM Data Viewer")
    data_option = st.selectbox(
        "Choose a dataset to explore",
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        energy_filter = st.slider("Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        st.dataframe(
            physics_data[physics_data["Energy (MeV)"].between(*energy_filter)]
        )

    elif data_option == "Astronomy Observations":
        brightness_filter = st.slider("Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        st.dataframe(
            astronomy_data[astronomy_data["Brightness (Magnitude)"].between(*brightness_filter)]
        )

    else:
        temp_filter = st.slider("Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Humidity (%)", 0, 100, (0, 100))
        st.dataframe(
            weather_data[
                weather_data["Temperature (°C)"].between(*temp_filter) &
                weather_data["Humidity (%)"].between(*humidity_filter)
            ]
        )

    # Contact Section
    st.header("Contact Information")
    st.write("📧 jane.doe@example.com")
