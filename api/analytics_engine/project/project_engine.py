from ..base import DataAnalyzer

class ProjectEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def analyze_projects(self):
    """
    Analyzes project trends from the provided JSON data.

    Args:
        data: A list of dictionaries containing user information.

    Prints insights about:
        - Most common project names and descriptions
        - Technologies frequently used across projects
    """
    project_name_counts = {}
    project_desc_counts = {}
    tech_usage = {}

    for profile in self.data:
      for project in profile["projects"]:
        # Track project name occurrences
        project_name = project["project_name"]
        if project_name in project_name_counts:
          project_name_counts[project_name] += 1
        else:
          project_name_counts[project_name] = 1

        # Track project description occurrences (considering uniqueness)
        project_desc = project["description"]
        if project_desc not in project_desc_counts:
          project_desc_counts[project_desc] = 1

        # Track technology usage across projects
        for tech in project.get("technologies_used", []):
          if tech in tech_usage:
            tech_usage[tech] += 1
          else:
            tech_usage[tech] = 1

    # Print insights
    print("\nMost Common Project Names:")
    # Sort by count (descending) and pick top N (modify as needed)
    sorted_names = sorted(project_name_counts.items(), key=lambda item: item[1], reverse=True)[:5]
    for name, count in sorted_names:
      print(f"- {name}: {count}")

    print("\nProject Descriptions (Unique):")
    # Print a sample of unique descriptions (modify as needed)
    for desc, count in project_desc_counts.items():
      print(f"- {desc}")
      break  # Print only the first unique description (as an example)

    print("\nTechnologies Frequently Used in Projects:")
    # Sort by usage (descending) and pick top N (modify as needed)
    sorted_tech = sorted(tech_usage.items(), key=lambda item: item[1], reverse=True)[:10]
    for tech, usage in sorted_tech:
      print(f"- {tech}: {usage}")

  def get_all(self):
    results = {}
    results['university_count'] = self.get_all_skills()
    results['students_per_university'] = self.find_most_frequent_skills()
    return results