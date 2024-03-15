import streamlit as st
import pandas as pd


def display_table(data):
    # Sample DataFrame (replace with your actual data)
    data = {key: [data[key]] for key in data.keys()}
    df = pd.DataFrame(data)

    # Display the DataFrame in Streamlit
    st.dataframe(df)
