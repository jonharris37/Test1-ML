import streamlit as st

st.title('Machine Learning App')

st.write('My first ML learning app!')

# add a checkbox ( user interaction)
checkBox = st.checkbox("Display text")
if checkBox:

st.text("Checkbox on!)

