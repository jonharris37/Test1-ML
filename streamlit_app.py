import streamlit as st
import pandas as pd  # ✅ correct import

st.title('Machine Learning App')
st.write('Data science Project')

checkBox = st.checkbox("Display text")

st.title(" My ML App")

if st.checkbox('Show text'):
    st.text("Checkbox on!")

# add side checkbox
checkboxSidebar = st.sidebar.checkbox("Display another text")

if checkboxSidebar:
    st.info("Sidebar checkbox information!")

url = file:///C:/Users/echo2/AppData/Local/Temp/lu683281nvxe.tmp/lu683281nvxk.tmp/powerElectricGeneration%20(6)%20(3).htm

try:
    df = pd.read_excel(url)
    st.success("Excel file loaded successfully!")
    st.write(df.head())  # Show the first few rows
except Exception as e:
    st.error(f"Error loading Excel file: {e}")














