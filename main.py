from sorter.sorter import read_csv, write_csv, sort_data
import config
import os

def main():
    print("Загрузка данных...")
    data = read_csv(config.INPUT_FILE)

    if not data:
        print("Файл пуст")
        return

    print(f"Сортировка по колонке: {config.SORT_COLUMN}")
    sorted_data = sort_data(data, config.SORT_COLUMN, config.ASCENDING)

    os.makedirs(os.path.dirname(config.OUTPUT_FILE), exist_ok=True)

    print("Сохранение результата...")
    write_csv(config.OUTPUT_FILE, sorted_data, sorted_data[0].keys())

    print("Готово!")

if __name__ == "__main__":
    main()