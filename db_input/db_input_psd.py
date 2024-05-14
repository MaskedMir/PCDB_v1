import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS storage_parameters (
                name TEXT,
                type TEXT,
                capacity TEXT,
                interface TEXT,
                form_factor TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('storage_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO storage_parameters
                        (name, type, capacity, interface, form_factor, price)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                    (row['name'], row['type'], row['capacity'], row['interface'], row['form_factor'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
