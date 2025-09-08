import streamlit as st

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











