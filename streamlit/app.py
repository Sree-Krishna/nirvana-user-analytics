import streamlit as st
from handle_requests import *
from utils import *

def create_sidebar():
  """Creates the sidebar for navigation."""
  sections = ["University & Student Statistics",
              "Skills Analysis",
              "Work Experience Insights",
              "Education Trends",
              "Certifications Analytics",
              "Project Analysis",
              "Language Proficiency",
              "Sentiment Analysis on Summaries",
              "Temporal Analysis",
              "Collaboration Patterns",
              "Geospatial Analytics"]
  selected_analysis = st.sidebar.selectbox("Choose Analysis", sections)
  return selected_analysis

def display_university_student_analysis():
    """Displays visualizations and data for university and student analysis."""
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_university_student_analysis()

        # Update placeholder with actual content
        st.subheader("Number of Students per University")
        display_chart(data)  # Call utility function for chart

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")
  

  # Add more visualizations or data tables here

def display_skills_analysis():
  """Displays visualizations and data for skills analysis."""
  st.subheader("Most Frequent Skills")

  # Add more visualizations or data tables here

def display_work_experience_analysis():
  """Displays visualizations and data for work experience analysis."""
  st.subheader("Average Work Experience Duration")

  # Add more visualizations or data tables here


def main():
    selected_analysis = create_sidebar()
    st.title("Nirvana Analytics Engine")
    if selected_analysis == "University & Student Statistics":
        display_university_student_analysis()
    elif selected_analysis == "Skills Analysis":
        display_skills_analysis()
    else:
        display_work_experience_analysis()

if __name__ == "__main__":
  main()
