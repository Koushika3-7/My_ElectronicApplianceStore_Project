import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='koushi$37',database='Electronic_Appliance_Store')
my_cursor=my_db.cursor()
def Pass_wd():
    passwd=input('Set your Password:')
    confirm_pass=input('Re-enter your password for confirmation:')
    if passwd==confirm_pass:
        return passwd
    else:
        print('Your passwords does not match.Please enter correct password')
        Pass_wd()
        
def Sign_up():
    user_mail=input('Enter your mail id:')
    crct_pass=Pass_wd()
    print('Your account is being created')
    name=input('Please set a username: ')
    cus_address=input('Enter your address for delivery: ')
    query1='insert into UserDetails(Name,Mail_id,Password,Address)\
         values(%s,%s,%s,%s)'
    val=(name,user_mail,crct_pass,cus_address)
    my_cursor.execute(query1,val)
    my_db.commit()
    print('Successful Sign-up')
    print('------------------------------------------------------------------------')
    return name

def Sign_in():
    id_cus=input('Enter your mail id:')
    q6='select exists(select * from UserDetails where Mail_id=%s)'
    my_cursor.execute(q6,(id_cus,))
    rj=my_cursor.fetchall()
    if(rj[0][0]==1):
        pass1=input('Enter your password:')
        id_cus1=(id_cus,)
        q='select Password,Name from UserDetails where Mail_id=%s'
        my_cursor.execute(q,id_cus1)
        r=my_cursor.fetchall()
        if r[0][0]==pass1:
            print('Successfully logged in')
            print('-----------------------------------------------------------------------')
            return r[0][1]
        else:
            print('Your Sign-in Details are wrong.Sign-in again')
            Sign_in() 
    else:
        print('User mail does not exist.Sign-in again')
        Sign_in()
            
    
