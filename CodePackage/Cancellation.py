import random
import mysql.connector
my_db5=mysql.connector.connect(host='localhost',user='root',password='koushi$37',database='Electronic_Appliance_Store')
my_cursor5=my_db5.cursor()
def to_cancel(user):
    que3='select exists(select * from CustomerpurchaseDetails where Name=%s)'
    my_cursor5.execute(que3,(user,))
    rr=my_cursor5.fetchall()
    if(rr[0][0]==0):
        print('----------------------------------------------------------------------------------')
        print('Nothing to cancel')
        print('You have not booked anything')
    else:
        qu4='select Details,Total_price,modelno_list,quantity_list from CustomerPurchaseDetails where Name=%s'
        my_cursor5.execute(qu4,(user,))
        r5=my_cursor5.fetchall()
        print('--------------------------------------------------------------')
        print('Purchase Details: ')
        a=r5[0][0].split(',')
        for i in a:
            print(i)
        print('-------------------------------------------------------------')
        print('Total cost:',r5[0][1])
        print('--------------------------------------------------------------')
        print('Are you sure you want to cancel your order?, Type yes or no ')
        vvv=input()
        if(vvv=='yes'):
            print('Enter the otp generated to your mail_id:')
            otp1=random.randrange(1000,5000)
            print(otp1)
            otp_user1=int(input('Enter OTP:'))
            if(otp1==otp_user1):
                print('Your order is successfully cancelled!!!')
                print('If paid you will be refunded soon')
                b=r5[0][2].strip('[').strip(']').split(',')
                c=r5[0][3].strip('[').strip(']').split(',')
                l1=[int(i) for i in b] #model_no
                l2=[int(i) for i in c] #quantity
                for j in range(len(b)):
                    qqq='select stock_available from Product where Model_No=%s'
                    ttt=(l1[j],)
                    my_cursor5.execute(qqq,ttt)
                    rrr=my_cursor5.fetchall()
                    av=rrr[0][0]+l2[j]
                    qq='update Product set stock_available=%s where Model_No=%s'
                    tt=(av,l1[j])
                    my_cursor5.execute(qq,tt)
                    my_db5.commit()
                    qq1='delete from CustomerPurchasedetails where Name=%s'
                    my_cursor5.execute(qq1,(user,))
                    my_db5.commit()
            else:
                print('Your OTP is wrong. Re-do the process')
                to_cancel(user)

        else:
            exit
        
        