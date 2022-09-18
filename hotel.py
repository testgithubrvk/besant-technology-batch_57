import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", 
    user="root",
    password="raghuljeevi@123",
    database="hotel"
)


mycursor=mydb.cursor()
#mycursor.execute("create database hotel")
#print("success")
#mycursor.execute("create table customer_data(customer_name varchar(255),address varchar(255),indate varchar(255),outdate varchar(255))")
#print("created")
#mycursor.execute("create table roomtype(sno varchar(255),roomtype varchar(255),rent int)")

#print("success")
def customer_register():
    name=input("enter name:")
    address=input("enter address")
    indate=input("enter your check in date:")
    outdate=input("enter your check out date:")
    sql="insert into customer_data(customer_name,address,indate,outdate) values (%s,%s,%s,%s)"
    val=(name,address,indate,outdate)
    mycursor.execute(sql,val)
    mydb.commit()
#customer_register()
def roomtypeview():
    print("do you want to see roomtype")
    print("press 1 for yes")
    press=int(input("enter the option:"))
    if press==1:
        sql="select* from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for r in rows:
            print(r)

    #sno=int(input("enter your sno:"))
    #roomtype=input("enter roomtype")
    #rent=int(input("enter your roomrent:"))
    #sql="insert into roomtype(sno,roomtype,rent) values(%s,%s,%s)"
    #val=(sno,roomtype,rent)
    #mycursor.execute(sql,val)
    #mydb.commit()
    
    
def roomrent():
    print("1.type 1--->RS 1000")  
    print("2.type 2--->RS 1500")  
    print("3.type 3--->RS 2000")  
    print("4.type 4--->RS 2500")
    type_1=1000
    type_2=1500
    type_3=2000
    type_4=2500
    x=int(input("enter your choice:"))
    #days=input("how many days you want:") 

    if x==1:
        print("you have choosen room type 1")
        days=int(input("how many days you want:") )
        total=type_1*days
        print(f"your room rent is :",total)
      
    elif x==2:
        print("you have choosen room type 2")
        days=int(input("how many days you want:") )
        total=type_2*days
        print(f"your room rent is: rs.{total}")
    elif x==3:
        print("you have choosen room type 3")
        days=int(input("how many days you want:") )
        total=type_3*days
        print(f"your room rent is rs.{total}")
    elif x==4:
        print("you have choosen room type 4")
        days=int(input("how many days you want:") )
        total=type_4*days
        print(f"your room rent is rs.{total}")
    else:
        print("choose the option correctly")
#mycursor.execute("create table restaurent(sno int,itemname varchar(255), itemrate int)")
#print("created") 
def restaurentview():
    print("do you want to see restaurent menu")
    print("press 1 for yes")
    press=int(input("enter the option:"))
    if press==1:
        sql="select* from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    #sno=int(input("enter your sno:"))
    #itemname=input("enter itemname")
    #itemrate=int(input("enter your itemrate:"))
    #sql="insert into restaurent(sno,itemname,itemrate) values(%s,%s,%s)"
    #val=(sno,itemname,itemrate)
    #mycursor.execute(sql,val)
    #mydb.commit()
    print("********welcome to RJ restaurant********")

    tiffen =["parota","idly","dosa","pongal","poori"]


    your_order=input("enter your order :")
    parota_amount=15
    idly_amount=15
    dosa_amount=20
    pongal_amount=30
    poori_amount=30


    if your_order in tiffen:

        print(f"yes your {your_order} is available")
        order_count=int(input(f"how many {your_order} you want:"))
        if your_order=="parota":

            total=parota_amount*order_count
            print(f"your total bill is Rs.{total}")
            
        if your_order=="idly":
            total=idly_amount*order_count
            print(f"your total bill is Rs.{total}")
        elif your_order=="dosa":
            total=dosa_amount*order_count
            print(f"your total bill is Rs.{total}")
        elif your_order=="poori":
            total=poori_amount*order_count
            print(f"your total bill is Rs.{total}")
        elif your_order=="pongal":
            total=pongal_amount*order_count
            print(f"your total bill is Rs.{total}")
                   
    
    meals=["halfmeals","fullmeals"]  
    
    half_meals_amt=90
    full_meals_amt=180   
    if  your_order in meals:
        print(f"yes your {your_order} is available")
        order_count=int(input(f"how many {your_order} you want:"))
        if your_order=="halfmeals":
            total=half_meals_amt*order_count
            print(f"your total bill is Rs.{total}")
        elif your_order=="fullmeals":
            total=full_meals_amt*order_count
            print(f"your total bill is Rs.{total}")
        else:
             print(" sorry your order is not available choose your menu from available menu item") 


    def menuset():
        print("1.To enter customer data")
        print("2.To view room type")
        print("3.To calculate room rent")
        print("4.restaurent")
        print("5.exit")

userinput=int(input("select the option:"))
        
if userinput==1:
    customer_register()
elif userinput==2:
    roomtypeview()
elif userinput==3:
    roomrent() 
elif userinput==4:
    restaurentview()     
elif userinput==5:
    exit() 



                                
                                    

