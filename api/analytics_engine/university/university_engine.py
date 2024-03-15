from ..base import DataAnalyzer

class UniversityEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def get_user_universities(self):
    """Extracts a list of universities attended by all users."""
    universities = []
    for user in self.data:
      for education in user["education"]:
        universities.append(education["university"])
    return universities

  def count_unique_universities(self):
    """Counts the number of unique universities in the dataset."""
    return len(set(self.get_user_universities()))

  def count_students_per_university(self):
    """Calculates the number of students associated with each university."""
    university_counts = {}
    for univ in self.get_user_universities():
      if univ not in university_counts:
        university_counts[univ] = 0
      university_counts[univ] += 1
    return university_counts
  
  def get_all(self):
    results = {}
    results['university_count'] = self.count_unique_universities()
    results['students_per_university'] = self.count_students_per_university()
    return results
