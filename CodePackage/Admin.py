import random
import mysql.connector
my_db2=mysql.connector.connect(host='localhost',user='root',password='koushi$37',database='Electronic_Appliance_Store')
my_cursor2=my_db2.cursor()
def to_add1():
    prod=input('Enter the product to add: ')
    model=input('Enter the model to add: ')
    model_no=int(random.randrange(1000,2000))
    desc=input('Enter the description: ')
    price=input('Enter the price of the product: ')
    stock=input('Enter the stock available: ')
    ratings=3
    q2='insert into Product (Prod_name,Model,Model_No,Description,Price,Stock_available,ratings)\
        values(%s,%s,%s,%s,%s,%s,%s)'
    val2=(prod,model,model_no,desc,price,stock,ratings)
    my_cursor2.execute(q2,val2)
    my_db2.commit()
    print('Product Added !')
    print('-------------------------------------------------------------------------')
    y3=input('Do you want to add some other product? type yes or no: ')
    if y3=='yes':
        to_add1()
    else:
        exit()

def to_delete1():
    val20=int(input('Enter the Model number of the product you want to delete: '))
    q3='delete from Product where Model_No=%s'
    my_cursor2.execute(q3,(val20,))
    my_db2.commit()
    print('Product Deleted !')
    print('--------------------------------------------------------------------')
    y2=input('Do you want to delete some other product? type yes or no: ')
    if y2=='yes':
        to_delete1()
    else:
        exit()

def to_modify1():
    val10=int(input('Enter the Model number of the product you want to modify: '))
    print('Enter 1 to modify description of a product')
    print('Enter 2 to modify price of a product')
    print('Enter 3 to modify stock available of a product')
    val11=int(input())
    if val11==1:
        val8=input('Enter the new description: ')
        q4='update Product set Description=%s where Model_No=%s'
        tup8=(val8,val10)
        my_cursor2.execute(q4,tup8)
        my_db2.commit()
    elif val11==2:
        val9=int(input('Enter the new Price: '))
        q5='update Product set Price=%s where Model_No=%s'
        tup9=(val9,val10)
        my_cursor2.execute(q5,tup9)
        my_db2.commit()
    else:
        val7=int(input('Enter the new no. of stock available: '))
        q6='update Product set Stock_available=%s where Model_No=%s'
        tup7=(val7,val10)
        my_cursor2.execute(q6,tup7)
        my_db2.commit()
    print('Changes Updated!')
    print('-------------------------------------------------------------------')
    y1=input('Do you want to modify some other product? type yes or no: ')
    if y1=='yes':
        to_modify1()
    else:
        exit()