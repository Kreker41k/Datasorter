import csv

def read_csv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(file_path, data, fieldnames):
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def sort_data(data, column, ascending=True):
    try:
        return sorted(
            data,
            key=lambda x: int(x[column]) if x[column].isdigit() else x[column],
            reverse=not ascending
        )
    except KeyError:
        raise ValueError(f"Column '{column}' not found in data")