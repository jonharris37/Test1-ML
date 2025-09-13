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













