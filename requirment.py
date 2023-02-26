import os
import sqlite3
opn = open('emails.db', 'w')
opn.close()
os.system("pip install tkinter")
os.system("pip install sqlite3")
os.system("pip instaal qrcode")
conn = sqlite3.connect('emails.db')
cursor = conn.cursor()
#Creating table as per requirement
sql ='''CREATE TABLE "mailiste" (
	"id"	TEXT,
	"email"	INTEGER,
	"passd"	INTEGER
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
conn.close()