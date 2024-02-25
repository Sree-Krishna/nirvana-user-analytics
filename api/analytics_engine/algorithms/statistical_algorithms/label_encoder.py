import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encoder(input_csv_path, column_name, output_csv_path):
    """
    Label encodes a specified column in a CSV file and saves the result in another CSV file.

    Parameters:
    - input_csv_path (str): Path to the input CSV file.
    - column_name (str): Name of the column to be label encoded.
    - output_csv_path (str): Path to the output CSV file to store the results.

    Returns:
    None
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)

    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()

    # Fit and transform the specified column using label encoding
    encoded_labels = label_encoder.fit_transform(df[column_name])

    # Create a new DataFrame with the original column and encoded labels
    result_df = pd.DataFrame({f"{column_name}_encoded": encoded_labels, column_name: df[column_name]})

    # Save the result to the output CSV file
    result_df.to_csv(output_csv_path, index=False)
    print(f"Label encoding completed. Results saved to: {output_csv_path}")


label_encoder(
    "/Users/devshah/Desktop/The Nirvana Labs/nirvana-user-analytics/data/attribute_structures/education.csv",
    "university",
    "/Users/devshah/Desktop/The Nirvana Labs/nirvana-user-analytics/state/education/university_labels.csv"
)

