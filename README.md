# mysqlvault
App for managing passwords stored on mysql database.

In the database passwords are encrypted using SHA256 with salt.
App decrypts them using provided key after they are downloaded.

You can create your own database with all needed tables using database.py script.
