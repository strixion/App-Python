import sqlite3

def add_restaraunt(restaraunt,data,products,Popular_dish,summ,data_add):
    conn = sqlite3.connect('dataset_strx.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO RESTAURANTS (Restaurant,data,products,popular_dish,summ,data_add) VALUES (?,?,?,?,?,?)',
                                            (restaraunt,data,products,Popular_dish,summ,data_add))
    conn.commit()
    conn.close()

