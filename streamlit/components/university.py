import streamlit as st
from .utils import *

def display_text():
    pass

def main(university_data):
    st.subheader("University Analysis")
    display_table(university_data)  # Call utility function for chart