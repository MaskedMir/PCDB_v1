import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS psu_parameters (
                name TEXT,
                power TEXT,
                lvl TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('psu_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO psu_parameters
                        (name, power, lvl, price)
                        VALUES (?, ?, ?, ?)''',
                    (row['name'], row['power'], row['lvl'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
