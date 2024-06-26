def extract_data(source: str):
    print(f"Extracting data from {source}")
    data = []
    try:
        with open(source, 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                record = dict(zip(headers, values))
                data.append(record)
    except FileNotFoundError:
        print(f"File {source} not found.")
    return data
