import streamlit as st

st.title('Machine Learning App')

st.write('My first ML learning app!')
checkBox = st.checkbox("Display text")

st.title(" My ML App")

if st.checkbox('Show text'):
    st.text("Checkbox on!")

# add side checkbox
checkboxSidebar = st.sidebar.checkbox






