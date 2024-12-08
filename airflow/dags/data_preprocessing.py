from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os

def process_data():
    raw_data_path = 'raw_data.csv'
    processed_data_path = 'processed_data.csv'  # Removed leading space in the file name

    # Load the raw data
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        raise Exception(f"Raw data file '{raw_data_path}' not found. Ensure it exists before preprocessing.")

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Ensure required columns exist
    required_columns = ['Temperature', 'Wind Speed']
    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Column '{col}' not found in the raw data.")

    # Scale the relevant columns
    scaler = MinMaxScaler()
    df[['Temperature', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Wind Speed']])

    # Save the processed data
    df.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")

if __name__ == "__main__":
    process_data()
