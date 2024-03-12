from fastapi import FastAPI
from uvicorn import run  # For running the application

# Importing routers
from endpoints import university_endpoint  
app = FastAPI()

app.include_router(university_endpoint.router)

# Optional configuration (e.g., documentation, middleware)


def run_app():
  """Starts the FastAPI application in development mode."""
  run("main:app", host="0.0.0.0", port=8000, reload=True)  # Change host/port as needed


if __name__ == "__main__":
  run_app()
