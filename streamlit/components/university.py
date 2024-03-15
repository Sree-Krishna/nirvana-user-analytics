import streamlit as st
from .utils import *
import pandas as pd

def display_university_distribution(data):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Student Count'])

    # Optional: Sort by student count (descending)
    df = df.sort_values(by='Student Count', ascending=True)
    st.bar_chart(df)

def main(university_data):
    st.subheader("University Analysis")
    st.write(f"The total number of unique universities are:  {university_data['university_count']}")
    st.subheader("Student count in universities")
    display_university_distribution(university_data['students_per_university'])  # Call utility function for chart