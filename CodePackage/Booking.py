import random
import mysql.connector
my_db1=mysql.connector.connect(host='localhost',user='root',password='koushi$37',database='Electronic_Appliance_Store')
my_cursor1=my_db1.cursor()
list1=[]#price
list2=[]#model no
list3=[]#details
list4=[]#quantity
def payment(username):
    print('-------------------------------------------------------')
    print('Your final list:')
    if len(list3)==0:
        print('Your list is empty')
        to_search(username)
    else:
        for i in list3:
            print(i)
        print('---------------------------------------------------')
        print('Total Cost:',sum(list1))
        print('-----------------------------------------------------')
        print('Payment Process')
        qs='select Mail_id from UserDetails where Name=%s'
        my_cursor1.execute(qs,(username,))
        rt=my_cursor1.fetchall()
        q2='insert into CustomerpurchaseDetails(Name,Mail_id,Details,Total_price,modelno_list,quantity_list)\
            values(%s,%s,%s,%s,%s,%s)'
        tupl=(username,rt[0][0],str(list3),sum(list1),str(list2),str(list4))
        my_cursor1.execute(q2,tupl)
        my_db1.commit()
        print('-------------------------------------------------------------------')
        print('Payment Mode')
        print('Enter 1 for cash on delivery')
        print('Enter 2 for card payment')
        val3=int(input())
        if val3==1:
            print('Your order is placed. You will receive your products in a week')
        else:
            input('Enter your card no.')
            input('Enter card holder name:')
            input('Enter CVV:')
            print('Enter the otp generated to your mail_id:')
            otp=random.randrange(1000,5000)
            print(otp)
            otp_user=int(input('Enter OTP:'))
            if(otp==otp_user):
                print('Payment Successful...!!! You will receive your products in a week')
            else:
                print('Your OTP is incorrect. Re-do payment process')
                payment(username)
        print('--------------------------------------------------')
    print('Thank you for shopping !!!!')

def rem_prod(username):
    va=int(input('Enter the Model number of the product to remove: '))
    qu=int(input('Enter the quantity you want to remove'))
    if va in list2:
        t=list2.index(va)
        que1='select stock_available,Price,Model from Product where Model_No=%s'
        tu1=(va,)
        my_cursor1.execute(que1,tu1)
        re=my_cursor1.fetchall()
        list4[t]-=qu
        avai=re[0][0]+qu
        if(list4[t]==0):
            list2.remove(va)
            list1.pop(t)
            list3.pop(t)
            list4.pop(t)
        else:
            t1=re[0][1]*qu
            list1[t]-=t1
            s1='Model: ' + re[0][2] +'  Model No: '+ str(va)+ '  Quantity: '+ str(qu)+'  Price: '+str(list1[t])
            list3[t]=s1
        que='update Product set stock_available=%s where Model_No=%s'
        tu=(avai,va)
        my_db1.commit()
    print('----------------------------------------------------------------------')
    print('Do you want to remove another product from your list?, Type yes or no')
    vr=input()
    if vr=='yes':
        rem_prod(username)
    else:
        payment(username)


def print_data(a):
    #print(a)
    print('Product No:',a[0])
    print('Model:',a[1])
    print('Model No:',a[2])
    print('Description:',a[3])
    print('Price:',a[4])
    print('Ratings {}/5'.format(a[5]))
    print('-----------------------------------------------------------')

def to_book(username):
    order=int(input('Enter the Product Number of the Product you want to buy: '))
    quan=int(input('Enter the quantity you want to buy: '))
    quer='select Price,stock_available,Model,Model_No from Product where Sl_no=%s'
    my_cursor1.execute(quer,(order,))
    for i in my_cursor1:
        if(quan<=i[1]):
            tup=(i[1]-quan,order)
            price_cust=(quan*i[0])
            list1.append(price_cust)
            list2.append(i[3])
            list4.append(quan)
            list3.append('Model: ' + i[2] + '  Model No: '+ str(i[3])+'  Quantity: '+ str(quan)+'  Price: '+str(price_cust))
            query3='update Product set stock_available=%s where Sl_no=%s'
            my_cursor1.execute(query3,tup)
            my_db1.commit()
            inp=input('Do you want to rate this product?, Type yes or no ')
            if(inp=='yes'):
                inp1=int(input('Enter your rating out of 5 for {}:'.format(i[2])))
                if(inp1>=3):
                    quer3='update Product set ratings=%s where Sl_no=%s'
                    tup1=(inp1,order)
                    my_cursor1.execute(quer3,tup1)
                    my_db1.commit()

        else:
            print('Sorry your product is not available')
            print('Search for some other related products')
            to_search(username)
    print('------------------------------------------------------------------')
    print('Do you want to continue shopping?, Type yes or no: ')
    v3=input().lower()
    if(v3=='yes'):
        to_search(username)
    else:
        print('Your Booking List: ')
        print('----------------------------------------------------------')
        for i in list3:
            print(i)
        print('----------------------------------------------------------------')
        print('Your total cost: ',sum(list1))
        print('----------------------------------------------------------------')
        print('Do you want to remove any product from the list?, type yes or no: ')
        vv=input()
        if(vv=='no'):
            payment(username)
        else:
            rem_prod(username)


def to_search(username):
    item_1=input('Search the product you want to purchase:').lower()
    item_=(item_1,)
    qu='select Sl_no,Model,Model_No,Description,Price,ratings from Product where Prod_name=%s'
    my_cursor1.execute(qu,item_)
    res1=my_cursor1.fetchall()
    for i in res1:
        print_data(i)
    print('To Book a product, type 1')
    print('To return back to search type 2')
    v=int(input())
    print('-------------------------------------------------------------')
    if v==2:
        to_search(username)
    else:
        to_book(username)

    
