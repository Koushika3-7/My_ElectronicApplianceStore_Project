import sys
sys.path.append(r"C:\Users\Koushika Vema\OneDrive\Desktop\Documents\ElectronicStore\CodePackage")
from Login import *
from Booking import*
from Admin import *
from Cancellation import *
print('Welcome to Python Store...!!!')
print('---------------------------------------------')
print('If you are an Admin, Type 0')
print('If you are an existing user, Type 1 to Sign-in')
print('If you are a new user, Type 2 to Sign-up')
val=int(input())
if val==0:
    print('Type 1 to add new product')
    print('Type 2 to delete a product')
    print('Type 3 to modify an existing product')
    vv1=int(input())
    if vv1==1:
        to_add1()
    elif vv1==2:
        to_delete1()
    else:
        to_modify1()
else:
    if val==1:
        x=Sign_in()
    else:
        x=Sign_up()
    print('Type 1 if you want to Book products')
    print('Type 2 if you want to Cancel products')
    deci=int(input())
    if(deci==1):
        to_search(x)
    else:
        to_cancel(x)


