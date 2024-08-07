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
                        self.cursor = self.connection.cursor(buffered=True)
                        
                
        def disconnect(self):
                self.connection.commit()
                self.cursor.close()
                self.connection.close()                        
                        
     
        def __init__(self):
                self.connect()
                # Apaga a tabela de usuários, se existir
                self.cursor.execute('''DROP TABLE IF EXISTS users;''')   

                # Criar a tabela de usuários conectados
                self.cursor.execute('''CREATE TABLE users (
                        id int AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) UNIQUE NOT NULL)''')        
                self.disconnect()
        def __del__(self):
                self.connection.close()
                self.cursor.close()
        
        def add_user (self,username):
                self.connect()
                
                #local pra usar o if p/ perguntar se o nome (unique) já existe e caso não, criar
                comando = "SELECT count(*) from users Where name = (%s); "
                self.cursor.execute(comando, [username])
                qtd_users = self.cursor.fetchone()[0]
                if (qtd_users != 0):
                         return
                
                comando = "INSERT INTO users (name) VALUES (%s);  "
                print (comando)

                print("adicionando na tabela")
                self.cursor.execute(comando, [username])

                
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