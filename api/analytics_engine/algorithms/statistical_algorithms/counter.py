import pandas as pd

def counter(input_csv_path, label_column, output_csv_path):
    """
    Counts the occurrences of each unique label in a specified column of a CSV file
    and stores the result in another CSV file.

    Parameters:
    - input_csv_path (str): Path to the input CSV file.
    - label_column (str): Name of the column containing labels to count.
    - output_csv_path (str): Path to the output CSV file to store the results.

    Returns:
    None
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)

    # Check if the specified column exists in the DataFrame
    if label_column not in df.columns:
        raise ValueError(f"Column '{label_column}' not found in the CSV file.")

    # Count the occurrences of each unique label
    label_counts = df[label_column].value_counts().reset_index()
    label_counts.columns = ['ID', 'Count']

    # Save the result to the output CSV file
    label_counts.to_csv(output_csv_path, index=False)
    print(f"Label occurrences counted. Results saved to: {output_csv_path}")



count = counter(
    "/Users/devshah/Desktop/The Nirvana Labs/nirvana-user-analytics/state/education/university_labels.csv",
    "university_encoded",
    "/Users/devshah/Desktop/The Nirvana Labs/nirvana-user-analytics/state/education/university_count.csv"
    )