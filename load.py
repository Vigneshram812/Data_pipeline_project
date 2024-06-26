import os

def load_data(destination: str, data: list):
    print(f"Loading data to {destination}")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    # Write data to file
    with open(destination, 'w') as f:
        for record in data:
            f.write(str(record) + '\n')