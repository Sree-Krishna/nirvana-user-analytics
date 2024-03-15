from ..base import DataAnalyzer

class ExperienceEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def get_all(self):
    results = {}
    results['average_experience'] = self.calculate_average_work_experience()
    results['job_titles'], results['companies'] = self.identify_most_common_job_titles_and_companies()
    return results

  def calculate_average_work_experience(self):
    import datetime
    """
    Calculates the average work experience in months for all profiles.

    Args:
        work_experience_data: A list of dictionaries containing work experience data.

    Returns:
        The average work experience in months (float).
    """
    total_experience_months = 0
    total_positions = 0
    for profile in self.data:
      for experience in profile["work_experience"]:
        if experience["end_date"]:
          end_date = datetime.datetime(experience["end_date"]["year"], experience["end_date"]["month"], 1)
        else:
          end_date = datetime.datetime.now()  # Assuming ongoing job if no end date
        if experience["start_date"]:
          start_date = datetime.datetime(experience["start_date"]["year"], experience["start_date"]["month"], 1)
        else:
          start_date = None  # Handle cases with no start date
        if start_date:
          total_experience_months += (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
          total_positions += 1
    if total_positions > 0:
      return total_experience_months / total_positions
    else:
      return 0  # Handle cases with no work experience data

  def identify_most_common_job_titles_and_companies(self):
    job_titles = {}
    companies = {}
    for profile in self.data:
      for experience in profile["work_experience"]:
        job_title = experience["job_title"]
        company = experience["company"]
        # Track occurrences in dictionaries
        if job_title in job_titles:
          job_titles[job_title] += 1
        else:
          job_titles[job_title] = 1
        if company in companies:
          companies[company] += 1
        else:
          companies[company] = 1

    # Sort job titles and companies by frequency (descending order)
    sorted_job_titles = sorted(job_titles.items(), key=lambda item: item[1], reverse=True)
    sorted_companies = sorted(companies.items(), key=lambda item: item[1], reverse=True)

    return job_titles, companies


  # def find_most_frequent_skills(self, n=10):
  #   """Finds the n most frequent skills across all users."""
  #   from collections import Counter
  #   all_skills = self.get_all_skills()
  #   skill_counts = Counter(all_skills)
  #   return skill_counts.most_common(n)

  # def get_all(self):
  #   results = {}
  #   results['average_experience'] = self.calculate_average_work_experience()
  #   results['job_titles'], results['companies'] = self.identify_most_common_job_titles_and_companies()
  #   return results