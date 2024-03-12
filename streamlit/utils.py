import streamlit as st
import pandas as pd

# Convert the dictionary to a list of lists for Streamlit table
def display_chart(data):
    # Sample DataFrame (replace with your actual data)
    data = {key: [data[key]] for key in data.keys()}
    df = pd.DataFrame(data)

    # Display the DataFrame in Streamlit
    st.dataframe(df)
