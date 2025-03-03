import sqlite3

conn = sqlite3.connect("image_processing.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS requests (
               id TEXT PRIMARY KEY, status TEXT, output_csv_url TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
               id INTEGER PRIMARY KEY AUTOINCREMENT, request_id TEXT, serial_number TEXT,
               product_name TEXT, input_image_urls TEXT, output_image_urls TEXT
)
''')

conn.commit()
conn.close()