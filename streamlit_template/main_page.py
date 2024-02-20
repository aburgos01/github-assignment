import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page") 

st.write("Click on a page to see racer or kart stats")

st.link = '[To my Github Pages](https://aburgos01.github.io/github-assignment/)'
st.markdown(st.link, unsafe_allow_html=True)