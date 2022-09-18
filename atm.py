
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", 
    user="root",
    password="raghuljeevi@123",
    database="atm_db"
)


mycursor=mydb.cursor()
#mycursor.execute("create database atm_db")
#print("success")
#mycursor.execute("create table atm_register(name varchar(255),account_no int,deposite_amt int,password int)")
#print("tab le ")
print("*****welcome to atm*****")
print("0.register")
print("1.login")
print("3.view data")
n=int(input("enter your number:"))
if n==0:
    name=input("enter your name:")
    acno=int(input("enter your account no:"))
    amt=int(input("enter your amount for deposite:"))
    paswrd=int(input("set your password:"))
    
    val=(name,acno,amt,paswrd)
    sql="insert into atm_register(name,account_no,deposite_amt,password) values (%s,%s,%s,%s)"
    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
if n==1:
    info=int(input("enter your account_no:")) 
    paswrd=int(input("enter your password:"))
    mycursor.execute("""select * from atm_register where account_no='%s'"""% (info))
    row=mycursor.fetchone()
    if mycursor.rowcount==1:
        mycursor.execute("""select * from atm_register where password='%s'"""% (paswrd))
        row=mycursor.fetchone()
        if mycursor.rowcount==1:
            print("login sucessfully")
            
            print("0.deposite")            
            print("1.withdrawl")
            print("2.exit")
            process=int(input("enter your processing choice:"))
            if process==0:
                a=int(input("enter the amount to be deposited in the account:"))
                mycursor.execute("select deposite_amt from atm_register  where password='%s'"""% (paswrd))
                column=mycursor.fetchone()
                x=list(column)
                for i in x:
                    z=(int(i))
                    c=z+a
            mycursor.execute("update atm_register set deposite_amt='%s' where password='%s'"%(c,paswrd))

            if process==1:

                a=int(input("enter the amount to be withdrawl in the account:"))
                mycursor.execute("""select deposite_amt from atm_register where password='%s'"""% (paswrd))
                column=mycursor.fetchone()
                x=list(column)
                for i in x:
                    z=(int(i))
                    c=z-a
            mycursor.execute("UPDATE atm_register SET deposite_amt='%s' where password='%s'"%(c,paswrd)) 

            if process==2:

                exit()

if n==3:
    def atm_registerview():

        print("do you want to data")
        print("press 1 for yes")
        #press=int(input("enter the option:"))
        if press==1:
            sql="select* from atm_register"
            mycursor.execute(sql)
            rows=mycursor.fetchall()
            for r in rows:
                print(r)
userinput=int(input("select the option:"))
        
if userinput==1:
    atm_registerview()            