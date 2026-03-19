# Datasorter

1. Клонируйте репозиторий:

  git clone https://github.com/your-username/datasorter.git

  cd Datasorter

2. Запустите программу:

  python main.py

3. Настройки находятся в файле config.py:

  INPUT_FILE = "data/input.csv"

  OUTPUT_FILE = "output/sorted.csv"

  SORT_COLUMN = "age"

  ASCENDING = True



**Обработка ошибок**

  Если колонка не найдена → будет вызвана ошибка

  Если файл пуст → программа завершится с предупреждением
