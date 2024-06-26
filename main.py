import os
from data_pipeline.extract import extract_data
from data_pipeline.transform import transform_data
from data_pipeline.load import load_data

def main():
    source = "example_data.txt"  # Update to match your actual data file
    destination = os.path.join("output", "data.txt")  # Using os.path.join for cross-platform compatibility

    # Extract
    data = extract_data(source)
    print(f"Extracted data: {data}")

    # Transform
    transformed_data = transform_data(data)
    print(f"Transformed data: {transformed_data}")

    # Load
    load_data(destination, transformed_data)
    print(f"Data loaded to {destination}")

if __name__ == "__main__":
    main()