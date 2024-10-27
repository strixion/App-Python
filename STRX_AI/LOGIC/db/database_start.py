import sqlite3

def create_db():
    conn = sqlite3.connect('dataset_strx.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS RESTAURANTS (
    id INTEGER PRIMARY KEY,
    Restaurant TEXT,
    data INTEGER,
    products TEXT,
    popular_dish TEXT,
    SUMM INTEGER,
    data_add INTEGER
    )
    ''')
    conn.commit()
    conn.close()