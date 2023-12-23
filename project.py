#bank balance project 27/9/2023


bal = 0
def check_bal():
    print('Total bal in your ac is:',bal)

def deposit(amt):
    global bal
    bal = bal + amt
    print(amt,'Rs. deposited!')

def withdraw(amt):
    global bal
    bal = bal - amt
    print(amt,'Rs. withdrawn!')
    if bal<=0:
        print('no bal')

while True:
    ch = int(input('\nEnter choice:\n1.check Balance\n2.Deposit\n3.Withdraw\n4.Exit'))
    if ch==1:
        check_bal()
    elif ch==2:
        d_amt = int(input('Enter amount to deposit:'))
        deposit(d_amt)
    elif ch==3:
        w_amt = int(input('Enter amount to withdraw:'))
        withdraw(w_amt)
    elif ch==4:
        print('exiting')
        break
    else:
        print('invaild choice')
