# Nirvana User Analytics

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Running the Analytics Engine](#running-the-analytics-engine)
  - [API Usage](#api-usage)
  - [UI Usage](#ui-usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Nirvana User Analytics project is a comprehensive data analytics engine designed to extract insights from user data stored in JSON format. It utilizes statistical, NLP-based, and AI-based filters and analytics to generate detailed reports. The primary focus is on analyzing information related to universities, students, skills, work experience, education, certifications, projects, and languages.

## Project Structure

The project follows a modular and composable structure for better code organization. Here is a breakdown of the key directories:

- **algorithms/**: Contains different types of algorithms and utility functions.
- **analytics_engine/**: Houses the analytics engine, organized by analytics types and includes a components directory for additional analytics.
- **api/**: Implements FastAPI for exposing backend APIs, with endpoints for different analytics categories.
- **ui/**: Includes a Streamlit app for a default UI and utility functions.
- **tests/**: Holds unit tests for algorithms, analytics engine, and components.
- **data/**: Contains the JSON file with user data.
- **docs/**: Documentation for algorithms, analytics engine, components, and usage instructions.
- **demo/**: Provides a script or document for running a demo.

## How to Use

### Setting Up the Environment

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/The-Nirvana-Labs/nirvana-user-analytics.git
   cd nirvana-user-analytics
   ```

2. **Install Dependencies:**
    ```bash
   pip install -r requirements.txt
   ```

### Running the Analytics Engine

1. **Run Analytics Engine:**
   ```bash
   python analytics_engine/university_stats/university_stats_engine.py
   ```

2. **Run Unit Tests:**
    ```bash
   pytest tests/
   ```

### API Usage

1. **Run FastAPI:**
   ```bash
   uvicorn api.main:app --reload
   ```

2. **Access API Documentation:**
    ```bash
   Open your browser and go to http://127.0.0.1:8000/docs
   ```
   
### UI Usage

1. **Run Streamlit App:**
   ```bash
   streamlit run ui/streamlit_app.py
   ```

2. **Access Streamlit UI:**
    ```bash
   Open your browser and go to http://localhost:8501
   ```
   
## Contributing
If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature.
3. Make your changes and commit them: git commit -m 'Add your feature'.
4. Push to the branch: git push origin feature/your-feature.
5. Submit a pull request.

## License
This project is licensed under the [MIT License](https://mit-license.org/).