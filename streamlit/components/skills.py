import streamlit as st
from .utils import *
import plotly.express as px 
import altair as alt

def display_skills_horizontal(data):
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Skill Count'])
    df.sort_values(by="Skill Count", inplace=True)
    # fig=px.bar(df,x='Skill Count', y=df.index, orientation='h',
    #          title="Number of Students per University (Horizontal Bar Chart)",
    #          labels={'index': 'Skill'})
    # fig.update_layout(bargap=0.5)
    # fig.update_traces(marker_line_width=1.5)
    # st.write(fig)
    data = pd.melt(df.reset_index(), id_vars=["index"])

    # Horizontal stacked bar chart
    chart = (
        alt.Chart(data)
        .mark_bar(size=10)
        .encode(
            x=alt.X("value", type="quantitative", title="Skill Count"),
            y=alt.Y("index", type="nominal", title="Skills", scale=alt.Scale(paddingInner=0)),
            color=alt.Color("variable", type="nominal", title=""),
            order=alt.Order("variable", sort="descending"),
        )
    )

    st.altair_chart(chart, use_container_width=True)

def display_skills_distribution(data):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Student Count'])

    # Optional: Sort by student count (descending)
    df = df.sort_values(by='Student Count', ascending=True)
    st.bar_chart(df)

    # # Display the DataFrame with a bar chart
    # st.dataframe(df.style.bar(color='skyblue'))

    # # Optional customizations (titles, labels, etc.)

def main(skills_data):
    st.subheader("Skills Analysis")
    st.write(f"The total number of unique skills are:  {len(skills_data['unique_skills'])}")
    st.subheader("Number of Students per skill")
    display_skills_distribution(skills_data['skill_distribution'])
    display_skills_horizontal(skills_data['skill_distribution'])