import sqlite3

conn = sqlite3.connect("PlayerDataB.dbf")
cr = conn.cursor()
try:
    cr.execute("""CREATE TABLE playerData (
 contact_id INTEGER PRIMARY KEY,
 first_name TEXT NOT NULL,
 last_name TEXT NOT NULL,
 email text NOT NULL UNIQUE,
 phone text NOT NULL UNIQUE
);""")
    print("PLAY. Created Table")
except:
    print("PLAY. Table Already Created")
conn.commit()
cr.execute("SELECT * FROM PlayerData")
#conn.close()