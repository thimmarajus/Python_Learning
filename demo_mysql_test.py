import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="123456",
 database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
#mycursor.execute("SELECT name, address FROM customers")

#myresult = mycursor.fetchall()
myresult = mycursor.fetchone()
#for x in myresult:
print(myresult)
#sql = "INSERT INTO customers(name,address) VALUES (%s, %s)"
"""val = [
    ("SrinivasaMadhu", "Taiwan"),
    ("RamkrishnaVenkatesh","Irrigepalli"),
    ("RamkrishnaSurya","Irrigenahally"),
    ("MudduSurya","Bangalore"),
    ("ManoharSurya","Bangalore"),
    ("TejasSurya","Bangalore"),
    ("NitinVenkatesh","Doddaballapura"),
    ("NethraVenkatesh","Doddaballapura"),
    ("JajiVenkatesh","Doddaballapura"),
    ("LingrajuMukundappa","Sira"),
    ("ManjaMukundappa","Irrigepalli")
]
mycursor.executemany(sql,val)

mydb.commit()"""

#print("last record inserted, ID:", mycursor.lastrowid)
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("CREATE TABLE customers_primar_key (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#print(x)
#print(mydb)
