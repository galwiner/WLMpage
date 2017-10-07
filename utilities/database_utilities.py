import sqlite3
import datetime
import random
import time


def create_database(database_path: str):
    """create the DB. deletes it if it already exists."""
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS WLM')
        ddl = "CREATE TABLE WLM(channel INT,time TEXT PRIMARY KEY,wavelength REAL);"  # defines the table in Data Definition Language
        cur.execute(ddl)
        conn.commit()


def update_db(database_path: str):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        now=time.time()
        date=str(datetime.datetime.fromtimestamp(now).strftime("%H:%M:%S"))
        chan=random.randint(1,8)
        wavelength=random.uniform(780.23,780.24)
        cur.execute("INSERT INTO WLM VALUES(?,?,?)",(chan,now,wavelength))
        conn.commit()


def fetchDB(database_path: str):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM WLM")
        data = cur.fetchall()
    return data


if __name__ == '__main__':
    DBPATH = 'wlm.db'
    create_database(DBPATH)
    [update_db(DBPATH) for i in range(1000)]
    # print(fetchDB(DBPATH))
