import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS gpu_parametrs (
                name TEXT,
                chip TEXT,
                memory_type TEXT,
                memory TEXT,
                bitrate TEXT,
                connection_interface TEXT,
                power TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('gpu.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO gpu_parametrs
                        (name, chip, memory_type, memory, bitrate, connection_interface, power, price)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                    (row['name'], row['chip'], row['memory_type'], row['memory'], row['bitrate'], row['connection_interface'], row['power'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
