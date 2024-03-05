
from pydantic import BaseModel

class University(BaseModel):
    name: str
    location: str
    courses: list[str]