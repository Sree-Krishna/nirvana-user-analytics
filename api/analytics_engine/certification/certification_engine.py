from ..base import DataAnalyzer

class CertificationEngine(DataAnalyzer):
  def __init__(self, data):
    super().__init__(data)

  def analyze_certifications(self):
    """
    Analyzes certification trends from the provided JSON data.

    Args:
        data: A list of dictionaries containing user information.

    Prints insights about:
        - Most frequently earned certifications
        - Distribution of certification acquisition over time (year-wise)
    """
    cert_counts = {}
    acquisition_years = {}

    # Check if certifications exist in user data
    has_certs = False
    for profile in self.data:
      if "certifications" in profile:
        has_certs = True
        break

    if not has_certs:
      print("No certification information provided.")
      return

    for profile in self.data:
      if "certifications" not in profile:
        continue
      for cert in profile["certifications"]:
        # Track certification occurrences
        if cert in cert_counts:
          cert_counts[cert] += 1
        else:
          cert_counts[cert] = 1

        # Extract acquisition year (assuming 'end_date' exists for certifications)
        acquisition_year = profile["certifications"][0]["end_date"]["year"]  # Assuming first cert for illustration
        if acquisition_year in acquisition_years:
          acquisition_years[acquisition_year] += 1
        else:
          acquisition_years[acquisition_year] = 1

    # Print insights (if certifications exist)
    if has_certs:
      # Find most frequent certifications (can be modified to return top N)
      most_frequent_certs = [cert for cert, count in cert_counts.items() if count == max(cert_counts.values())]

      print("\nMost Frequently Earned Certifications:")
      print(", ".join(most_frequent_certs))

      print("\nDistribution of Certification Acquisition Over Time:")
      for year, count in acquisition_years.items():
        print(f"- {year}: {count}")
      return  {'most_frequent': most_frequent_certs, 'acquisition_years': acquisition_years}

  def get_all(self):
    results = self.analyze_certifications()
    return results