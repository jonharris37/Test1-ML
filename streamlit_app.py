import streamlit as st
import pandas as pd

# Title and description
st.title("Machine Learning App")
st.write("Data Science Project")

# Checkbox in main page
if st.checkbox("Display text"):
    st.text("Checkbox on!")

# Checkbox in sidebar
if st.sidebar.checkbox("Display another text"):
    st.info("Sidebar checkbox information!")

# Load data
# Change the file path to your actual dataset location
file_path = "../datasetpowerElectricGeneration (6).xlsx"

try:
    dataset = pd.read_excel(file_path)
    st.subheader("Dataset Preview")
    st.dataframe(dataset.head())  # Show first rows
except FileNotFoundError:
    st.error(f"File not found: {file_path}")
except Exception as e:
    st.error(f"Error loading dataset: {e}")












