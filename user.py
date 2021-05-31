import mysql.connector
import crypt

class User():
        def __init__(self, address, port, username, password, encrypt_key):
                self.address = address
                self.port = port
                self.username = username
                self.password = password
                self.key = crypt.create_key(encrypt_key)

        def connect(self):
                self.db = mysql.connector.connect(
                        host = self.address,
                        port = self.port,
                        user = self.username,
                        password = self.password,
                        database = f'passwords_{self.username}',
                        ssl_disabled = False
                )
                self.c = self.db.cursor()

        def disconnect(self):
                self.db.close()

        def get(self, decrypt=False):
                self.connect()
                
                self.c.execute('SELECT * FROM passwords')
                row = self.c.fetchone()
                data = []
                while row is not None:
                        if decrypt:
                                raw_name = crypt.decrypt(row[2], self.key)
                                raw_pass = crypt.decrypt(row[3], self.key)
                                data.append((row[0], row[1], raw_name, raw_pass, row[4]))
                        else:
                                data.append((row[0], row[1], row[2], row[3], row[4]))
                        row = self.c.fetchone()
                return data

                self.disconnect()

        def insert(self, website, raw_name, raw_pass, image):
                self.connect()

                encrypted_name = str(crypt.encrypt(raw_name, self.key))
                encrypted_pass = str(crypt.encrypt(raw_pass, self.key))
                self.c.execute(f"INSERT INTO passwords (website, login, pass, image) VALUES (\"{website}\", \"{encrypted_name}\", \"{encrypted_pass}\", \"{image}\");")
                self.db.commit()

                self.disconnect()

        def delete(self, element_id):
                self.connect()

                self.c.execute(f"DELETE FROM passwords WHERE id = {element_id};")
                self.db.commit()

                self.disconnect()