from ..base import DataAnalyzer

class SkillsEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def get_all_skills(self):
    """Extracts a list of all unique skills mentioned by users."""
    skills = []
    for user in self.data:
      skills += user["skills"]
    return list(skills)

  def find_most_frequent_skills(self, n=10):
    """Finds the n most frequent skills across all users."""
    from collections import Counter
    skill_counts = {}
    for skills in self.get_all_skills():
      if skills not in skill_counts:
        skill_counts[skills] = 0
      skill_counts[skills] += 1
    return skill_counts

  def get_all(self):
    results = {}
    results['unique_skills'] = set(self.get_all_skills())
    results['skill_distribution'] = self.find_most_frequent_skills()
    return results
    