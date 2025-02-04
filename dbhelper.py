import sys

import mysql.connector
class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occurred. Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to database")

    def register(self, name, email, password):

        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        try:
            self.mycursor.execute("""
            SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'
            """.format(email,password))
            data = self.mycursor.fetchall()
            print(data)
            if len(data) == 0:
                print("Incorrect email/password")
            else:
                print("Hello",data[0][1])
        except:
            return -1
        else:
            return 1