import streamlit as st
from .utils import *
import altair as alt

def display_skills_horizontal(data):
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Job Count'])
    df.sort_values(by="Job Count", inplace=True)
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
            x=alt.X("value", type="quantitative", title="Job Count"),
            y=alt.Y("index", type="nominal", title="Experience", scale=alt.Scale(paddingInner=0)),
            color=alt.Color("variable", type="nominal", title=""),
            order=alt.Order("variable", sort="descending"),
        )
    )

    st.altair_chart(chart, use_container_width=True)

def display_skills_horizontaly(data):
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Count'])
    df.sort_values(by="Count", inplace=True)
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
            x=alt.X("value", type="quantitative", title="Count"),
            y=alt.Y("index", type="nominal", title="Companies", scale=alt.Scale(paddingInner=0)),
            color=alt.Color("variable", type="nominal", title=""),
            order=alt.Order("variable", sort="descending"),
        )
    )

    st.altair_chart(chart, use_container_width=True)

def main(experience_data):
    st.subheader('Experience Analysis')
    st.write(f"The average work experience in months is {experience_data['average_experience']}")
    st.write("Experience vs Count")
    display_skills_horizontal(experience_data['job_titles'])
    st.write("Companies vs Count")
    display_skills_horizontaly(experience_data['companies'])