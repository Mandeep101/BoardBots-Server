import sqlite3

connection = sqlite3.connect("TestData.db")
crsr = connection.cursor()

sql_command = """CREATE TABLE PlayerData (
playerID VARCHAR(30) PRIMARY KEY,
joining DATE,
cardsPlayed INTEGER);"""
crsr.execute(sql_command)
crsr.execute("""INSERT INTO PlayerData VALUES ("Mandeep", "2019-04-22", 65)""")

crsr.execute("SELECT * FROM PlayerData")

print(crsr.fetchall())

connection.commit()
connection.close()
