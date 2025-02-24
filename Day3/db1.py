import pymysql 
def connect_db():
    try:
        connection =pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='SamSql',charset='utf8')
        print('DB connected')
        return connection
    except:
        print("Error while connecting DB")
def disconnect_db(connection):
    try:
        print('DB disconnected')
        connection.close()
    except:
        print("Error while Disconnecting")
def insert_row():
    connection=connect_db()
    if connection:
        disconnect_db(connection)