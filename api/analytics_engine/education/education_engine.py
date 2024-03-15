from ..base import DataAnalyzer

class EducationEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def get_all_skills(self):
    """Extracts a list of all unique skills mentioned by users."""
    skills = set()
    for user in self.data:
      skills.update(user["skills"])
    return list(skills)

  def find_most_frequent_skills(self, n=10):
    """Finds the n most frequent skills across all users."""
    from collections import Counter
    all_skills = self.get_all_skills()
    skill_counts = Counter(all_skills)
    return skill_counts.most_common(n)

  def get_all(self):
    results = {}
    results['university_count'] = self.get_all_skills()
    results['students_per_university'] = self.find_most_frequent_skills()
    return results