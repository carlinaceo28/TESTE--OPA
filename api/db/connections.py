import mysql.connector
from mysql.connector import Error
import json


class db_connector:
        def connect(self):
                self.connection = mysql.connector.connect(
                        host='localhost',
                        database='banco_clientes',
                        user='root',
                        password='root')
                if self.connection.is_connected():
    
                        print("Conectado ao MySQL Serve ")
                        self.cursor = self.connection.cursor()
                        self.cursor.execute("select database();")
                        record = self.cursor.fetchone()
                
        def disconnect(self):
                self.connection.commit()
                self.cursor.close()
                self.connection.close()                        
                        
     
        def __init__(self):
                self.connect()
                # Criar a tabela de usuários conectados, se não existir
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id int AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL)''')        
                self.disconnect()
        def __del__(self):
                self.connection.close()
                self.cursor.close()
        
        def add_user (self,user):
                self.connect()
                z=json.loads(user)
                

                comando = "INSERT INTO users (name) VALUES ('%s')  " % ( z["nome"])
                print (comando)

                print("adicionado na tabela")
                self.cursor.execute(comando)

                
                self.disconnect()



                #comando = "INSERT INTO users (id ,name) 
                #VALUES ({z["cpf"]},{z["name"]})"({z["cpf"]},{z["name"]})


#mydb = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database, charset="utf8")
#cursor = mydb.cursor()
#query = "INSERT INTO tablename (text_for_field1, text_for_field2, text_for_field3, text_for_field4) VALUES (%s, %s, %s, %s)"
#cursor.execute(query, (field1, field2, field3, field4))
#mydb.commit()
#cursor.close()
#mydb.close()