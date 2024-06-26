def transform_data(data: list):
    # Placeholder for data transformation logic
    print("Transforming data")
    transformed_data = [{k: v.upper() if isinstance(v, str) else v for k, v in record.items()} for record in data]
    return transformed_data