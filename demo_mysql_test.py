import mysql.connector
<<<<<<< HEAD

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="123456"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#print(mydb)
=======
>>>>>>> eef60d88be294055f748d7c70acb657ee6edb9ab
