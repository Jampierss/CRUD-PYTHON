import mysql.connector
from tkinter import messagebox

class ConnectDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connectDB = None
    
    def connect(self):
        try:
            self.connectDB = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                ssl_disabled=True
            )
            print("Successfuly connection to the database!")
        except mysql.connector.Error as error:
            print("Something went wrong connecting to the database: ", error)
    
    def disconnect(self):
        if self.connectDB:
            self.connectDB.close()
            print("Successfully disconnecting to the database!")
    
    def execute_insert(self, table, id, model, year, color, capacity, power, type, transmission, price):
        sql = f"INSERT INTO {table}(id, model, year, color, engineCapacity, enginePower, engineType, transmission, price) VALUES({id},'{model}', '{year}', '{color}', {capacity},{power}, '{type}','{transmission}',{price})"
        self.commit_to_db(sql)
    
    def execute_delete(self, table, id):
        sql = f"DELETE FROM {table} WHERE id = {id}"
        self.commit_to_db(sql)
    
    def execute_update(self, table, id, model, year, color, capacity, power, engineType, transmission, price):
        sql = f"UPDATE {table} SET model='{model}', year='{year}', color='{color}', engineCapacity={capacity}, enginePower={power}, engineType='{engineType}',transmission='{transmission}', price={price} WHERE id={id}"
        cursor = self.connectDB.cursor()
        self.commit_to_db(sql)
    
    def commit_to_db(self, sql):
        cursor = self.connectDB.cursor()
        try:
            cursor.execute(sql)
            self.connectDB.commit()
            print("Query successfully executed")
            messagebox.showinfo("Successfully","Query successfully executed. Good Work!")
        except mysql.connector.Error as error:
            self.connectDB.rollback()
            print("Error executing the query:", error)
            messagebox.showerror("Error", "Duplicate ID entry, please try again!")


    def execute_select(self, table):
        sql = f"SELECT * FROM {table}"
        cursor = self.connectDB.cursor()
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as error:
            print("Error executing the query:", error)
            return []
        
    def __str__(self):
        data = self.execute_select("car")
        aux=""
        for row in data:
            aux += str(row)+"\n"
        return aux