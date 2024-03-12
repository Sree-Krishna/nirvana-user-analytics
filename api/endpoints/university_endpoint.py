from fastapi import APIRouter
from analytics_engine.university.university_engine import UniversityEngine
from model import load_data

router = APIRouter()

# Load user data (replace 'user_data.json' with your actual path)
data = load_data("data/test_user.json")
university_engine = UniversityEngine(data)

@router.get("/universities/count")
async  def get_all_universities_count():
  """FastAPI endpoint to retrieve the number of unique universities."""
  num_universities = university_engine.count_unique_universities()
  return {"number_of_universities": num_universities}

@router.get("/universities/students_per_university")
async def get_university_student_counts():
  """FastAPI endpoint to retrieve the number of students per university."""
  student_counts = university_engine.count_students_per_university()
  return {"university_student_counts": student_counts}
