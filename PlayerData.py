import sqlite3
import datetime

conn = sqlite3.connect("PlayerDataB.dbf")
cr = conn.cursor()
try:
    cr.execute("""CREATE TABLE PlayerData (
 playerID CHAR(40) PRIMARY KEY,
 joinDate DATE,
 gamesPlayed INTEGER,
 cardsPlayed INTEGER,
 forwardsPlayed INTEGER,
 leftsPlayed INTEGER,
 rightsPlayed INTEGER,
 hacksPlayed INTEGER,
 hackedPlayed INTEGER,
 batteriesPicked INTEGER,
 wins INTEGER,
 losses INTEGER,
 draws INTEGER
);""")
    print("PLAY. Created Table")
except:
    print("PLAY. Table Already Created")
conn.commit()
cr.close()
conn.close()

def readyPlayer(PlayerID):
    conn = sqlite3.connect("PlayerDataB.dbf")
    cr = conn.cursor()
    cr.execute("""SELECT playerID FROM PlayerData
WHERE playerID="%s\"""" % (PlayerID))
    if len(cr.fetchall())==0:
        cr.execute("""INSERT INTO PlayerData VALUES ("%s", "%s", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)""" % (PlayerID, datetime.date.today()))
    conn.commit()
    cr.close()
    conn.close()
    #Test if player exists, if not, add him to db
    
def GetStats(Data):
    PlayerID = ""
    StatText = ""
    conn = sqlite3.connect("PlayerDataB.dbf")
    cr = conn.cursor()
    for i in range(len(Data)):
        if Data[i] == ":":
            PlayerID = Data[i+1:]
            break
    cr.execute("SELECT * FROM PlayerData WHERE playerID=\"%s\"" % (PlayerID))
    #SQL that PlayerData
    RawData = cr.fetchall()
    print("PLAY. " + str(RawData))
    cr.close()
    conn.close()
    StatText = "%s joined BoardBots on %s playing a total of %i Games, Winning %i and Losing %i (with %i Draws). This player has played %i cards with %i being Forward, %i being Left, %i being Right and %i being Hack. The player has been hacked %i times and has picked up %i Batteries" % (RawData[0][0], RawData[0][1], RawData[0][2], RawData[0][10], RawData[0][11], RawData[0][12], RawData[0][3],RawData[0][4],RawData[0][5],RawData[0][6],RawData[0][7],RawData[0][8],RawData[0][9])
    return StatText