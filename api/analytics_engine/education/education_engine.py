from ..base import DataAnalyzer

class EducationEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def analyze_education_trends(self):
    """
    Analyzes education trends from the provided JSON data.

    Args:
        data: A list of dictionaries containing user information.

    Prints insights about:
        - Distribution of degrees obtained
        - Graduation date trends (year-wise)
        - Honors received by users
    """
    degree_counts = {}
    graduation_years = {}
    honors_received = set()

    for profile in self.data:
      for education in profile["education"]:
        degree = education["degree"]
        graduation_year = education["graduation_date"]["year"]
        honors = education.get("honors")  # Check if honors exist

        # Track degree occurrences
        if degree in degree_counts:
          degree_counts[degree] += 1
        else:
          degree_counts[degree] = 1

        # Track graduation years
        if graduation_year in graduation_years:
          graduation_years[graduation_year] += 1
        else:
          graduation_years[graduation_year] = 1

        # Track honors received (if any)
        if honors:
          honors_received.add(honors)
    results = {}
    results['degree_counts'] = degree_counts
    results['graduation_years'] = graduation_years
    results['honors_received'] = honors_received
    return results

  def get_all(self):
    results = self.analyze_education_trends()
    return results