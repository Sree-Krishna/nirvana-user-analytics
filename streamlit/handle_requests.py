import requests

def get_university_student_analysis():
  """Makes a request to the backend for university and student analysis data."""
  response = requests.get("http://localhost:8000/universities/count")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()
  # return {'university_counts': 10}

def get_skills_analysis_data():
  """Makes a request to the backend for skills analysis data."""
  response = requests.get("http://localhost:8000/student_skills")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

