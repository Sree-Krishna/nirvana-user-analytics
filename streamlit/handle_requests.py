import requests

def get_university_data():
  """Makes a request to the backend for university analysis data."""
  response = requests.get("http://localhost:8000/universities")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

def get_skills_data():
  """Makes a request to the backend for skills analysis data."""
  response = requests.get("http://localhost:8000/skills")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

def get_experience_data():
  """Makes a request to the backend for experience analysis data."""
  response = requests.get("http://localhost:8000/experience")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

def get_education_data():
  """Makes a request to the backend for education analysis data."""
  response = requests.get("http://localhost:8000/education")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

def get_certification_data():
  """Makes a request to the backend for certification analysis data."""
  response = requests.get("http://localhost:8000/certification")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()

def get_project_data():
  """Makes a request to the backend for project analysis data."""
  response = requests.get("http://localhost:8000/project")
  response.raise_for_status()  # Raise an exception for non-200 status codes
  return response.json()