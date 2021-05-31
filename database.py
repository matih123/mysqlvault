import mysql.connector
import string
import random

class Database():
        db = mysql.connector.connect(
                host='',
                user='',
                password=''
        )
        c = db.cursor()

        def create(self, name):
                password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(24))

                Database.c.execute(f'CREATE DATABASE passwords_{name};')
                Database.c.execute(f'CREATE TABLE `passwords_{name}`.`passwords` ( `id` INT(255) NOT NULL AUTO_INCREMENT , `website` VARCHAR(255) NOT NULL , `login` VARCHAR(255) NOT NULL , `pass` VARCHAR(255) NOT NULL, `image` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`), UNIQUE `u` (`login`)) ENGINE = InnoDB;')
                Database.c.execute(f'CREATE USER \'{name}\'@\'%\' IDENTIFIED BY \'{password}\';')
                Database.c.execute(f'GRANT ALL PRIVILEGES ON `passwords_{name}`.`passwords` TO \'{name}\'@\'%\';')
                Database.c.execute(f'FLUSH PRIVILEGES;')

                print(f'Created mysql user and database. Login: {name}, password: {password}')

        def delete(self, name):
                Database.c.execute(f'DROP DATABASE passwords_{name};')
                Database.c.execute(f'DROP USER \'{name}\'@\'%\';')

                print(f'Deleted mysql user and database. Login: {name}')
