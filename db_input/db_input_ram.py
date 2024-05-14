import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS ram_parameters (
                name TEXT,
                type TEXT,
                memory TEXT,
                power TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('ram_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO ram_parameters
                        (name, type, memory, power, price)
                        VALUES (?, ?, ?, ?, ?)''',
                    (row['name'], row['type'], row['memory'], row['power'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS ram_parameters (
                name TEXT,
                type TEXT,
                memory TEXT,
                power TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('ram_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO ram_parameters
                        (name, type, memory, power, price)
                        VALUES (?, ?, ?, ?, ?)''',
                    (row['name'], row['type'], row['memory'], row['power'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
