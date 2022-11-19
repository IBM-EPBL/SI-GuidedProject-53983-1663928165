import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('static/database/storage.db')
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists users(name varchar, email varchar, password varchar)")
        self.cur.execute("create table if not exists customer_complaint(name varchar, email varchar, complaint varchar)")
        self.cur.execute("create table if not exists admin(username varchar, password varchar)")
        self.cur.execute("create table if not exists agent(id int, name varchar)")
        # self.cur.execute("insert into admin values('admin', 'admin')")
        # self.cur.execute("insert into agent values(1, 'SANJAY')")
        # self.cur.execute("insert into agent values(2, 'ROGITH')")
        # self.cur.execute("insert into agent values(3, 'GOUTHAM')")
        self.con.commit()
    
    def creeateUser(self, name, email, password):
        self.cur.execute("insert into users values('" + name + "', '" + email + "', '" + password + "')")
        self.con.commit()

    def loginUser(self, email):
        self.cur.execute("select password from users where email = '" + email + "'")
        userData = self.cur.fetchone()
        return userData

    def loginAdmin(self, email):
        self.cur.execute("select password from admin where username = '" + email + "'")
        userData = self.cur.fetchone()
        return userData

    def registerComplaint(self, name, email, complaint):
        self.cur.execute("insert into customer_complaint values('" + name + "', '" + email + "', '" + complaint + "')")
        self.con.commit()

    def getAgents(self):
        self.cur.execute("select * from agent")
        userData = self.cur.fetchall()
        return userData

    def getComplaints(self):
        self.cur.execute("select * from customer_complaint")
        userData = self.cur.fetchall()
        return userData

    

    