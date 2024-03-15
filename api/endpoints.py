from fastapi import APIRouter
from analytics_engine.university.university_engine import UniversityEngine
from analytics_engine.skills.skills_engine import SkillsEngine
from analytics_engine.education.education_engine import EducationEngine
from analytics_engine.experience.experience_engine import ExperienceEngine
from analytics_engine.certification.certification_engine import CertificationEngine
from analytics_engine.project.project_engine import ProjectEngine
from analytics_engine.language.language_engine import LanguageEngine
from model import load_data

router = APIRouter()

# Load user data (replace 'user_data.json' with your actual path)
data = load_data("data/test_user.json")
university_engine = UniversityEngine(data)
skills_engine = SkillsEngine(data)
project_engine = ProjectEngine(data)
education_engine = EducationEngine(data)
experience_engine = ExperienceEngine(data)
certification_engine = CertificationEngine(data)
language_engine = LanguageEngine(data)


@router.get("/universities")
async  def get_university_analytics():
  university_engine_data = university_engine.get_all()
  return university_engine_data

@router.get("/skills")
async  def get_skills_analytics():
  skills_engine_data = skills_engine.get_all()
  return skills_engine_data

@router.get("/education")
async  def get_education_analytics():
  education_engine_data = education_engine.get_all()
  return education_engine_data

@router.get("/project")
async  def get_project_analytics():
  project_engine_data = project_engine.get_all()
  return project_engine_data

@router.get("/experience")
async  def get_experience_analytics():
  experience_engine_data = experience_engine.get_all()
  return experience_engine_data

@router.get("/certification")
async  def get_certificaiton_analytics():
  certification_engine_data = certification_engine.get_all()
  return certification_engine_data

@router.get("/language")
async  def get_language_analytics():
  language_engine_data = language_engine.get_all()
  return language_engine_data
