import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS cpu_parameters (
                name TEXT,
                technical_process TEXT,
                canals INTEGER,
                cores INTEGER,
                frequency REAL,
                cache INTEGER,
                tdp INTEGER,
                video_core TEXT,
                socket TEXT,
                ram_type TEXT,
                ram_canale TEXT,
                ram_frequency INTEGER,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('cpu.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO cpu_parameters
                        (name, technical_process, canals, cores, frequency, cache, tdp, video_core, socket, ram_type, ram_canale, ram_frequency, price)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (row['name'], row['technical_process'], row['canals'], row['cores'], row['frequency'], row['cache'], row['tdp'], row['video_core'], row['socket'], row['ram_type'], row['ram_canale'], row['ram_frequency'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
