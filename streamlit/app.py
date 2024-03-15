import streamlit as st
from handle_requests import *
from components import university, skills, experience, education, project, certification


SECTIONS = {"UNIVERSITY": "University & Student Statistics",
            "SKILLS": "Skills Analysis",
            "EXPERIENCE": "Work Experience Insights",
            "EDUCATION": "Education Trends", 
            "CERTIFICATION": "Certifications Analytics",
            "PROJECT": "Project Analysis",
            "LANGUAGE": "Language Proficiency",
            "SUMMARY": "Sentiment Analysis on Summaries"}
            # 'TEMPORAL": "Temporal Analysis",
            # 'UNIV": "Collaboration Patterns",
            # 'UNIV": "Geospatial Analytics"}

def create_sidebar():
  """Creates the sidebar for navigation."""  
  selected_analysis = st.sidebar.selectbox("Choose Analysis", SECTIONS.values())
  return selected_analysis

def university_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_university_data()
            university.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")
  
def skills_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_skills_data()
            skills.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")

def experience_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_experience_data()
            experience.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")

def education_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_education_data()
            education.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")

def certification_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_certification_data()
            certification.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")

def project_analysis():
    try:
        # Fetch data from the backend
        with st.spinner("Fetching data..."):
        # Fetch data from the backend
            data = get_project_data()
            project.main(data)

    except Exception as e:
        st.subheader("Loading Failed!")
        st.error(f"Error fetching data: {e}")

def main():
    # sidebar for navigation between various analysis
    st.title("Nirvana Analytics Engine")
    selected_analysis = create_sidebar()

    if selected_analysis == SECTIONS['UNIVERSITY']:
        university_analysis()
    elif selected_analysis == SECTIONS['SKILLS']:
        skills_analysis()
    elif selected_analysis == SECTIONS['EXPERIENCE']:
        experience_analysis()
    elif selected_analysis == SECTIONS['EDUCATION']:
        education_analysis()
    elif selected_analysis == SECTIONS['CERTIFICATION']:
        certification_analysis()
    elif selected_analysis == SECTIONS['PROJECT']:
        project_analysis()
    elif selected_analysis == SECTIONS['LANGUAGE']:
        # language_analysis()
        pass
    elif selected_analysis == SECTIONS['SUMMARY']:
        # summary_analysis()
        pass


if __name__ == "__main__":
  main()
