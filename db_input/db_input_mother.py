import csv
import sqlite3

# Соединяемся с базой данных
conn = sqlite3.connect('../pcdb.db')
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS motherboard_parameters (
                name TEXT,
                chipset TEXT,
                socket TEXT,
                ram_type TEXT,
                expansion_slots INTEGER,
                sata INTEGER,
                sata_version TEXT,
                m2 INTEGER,
                usb3_2 INTEGER,
                usb2_0 INTEGER,
                form_factor TEXT,
                price INTEGER
            )''')

# Открываем CSV-файл и вставляем данные в таблицу
with open('motherboard_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cur.execute('''INSERT INTO motherboard_parameters
                        (name, chipset, socket, ram_type, expansion_slots, sata, sata_version, m2, usb3_2, usb2_0, form_factor, price)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (row['name'], row['chipset'], row['socket'], row['ram_type'], row['expansion_slots'], row['sata'], row['sata_version'], row['m2'], row['usb3.2'], row['usb2.0'], row['form_factor'], row['price']))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
