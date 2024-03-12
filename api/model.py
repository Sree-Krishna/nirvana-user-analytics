
from pydantic import BaseModel
import json

def load_data(data_path):
  """Loads user data from a JSON file."""
  try:
    with open(data_path, "r") as f:
      data = json.load(f)
    return data
  except FileNotFoundError:
    raise Exception("User data file not found!")
  except json.JSONDecodeError:
    raise Exception("Invalid JSON format in user data file!")
  
class University(BaseModel):
    name: str
    location: str
    courses: list[str]