import streamlit as st
from .utils import *

def main(skills_data):
    st.subheader("Skills Analysis")
    print(skills_data)
    display_table(skills_data)  # Call utility function for chart