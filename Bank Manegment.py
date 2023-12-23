contact ={'555':'aaa','666':'bbb'}

while True:
    ch = int(input('\nenter a choice\n1.add new contact\n2.show all contact\n3.update your contact\n4.det contact\n5.exit'))
    if ch == 1:
        print('add new contact\n')
        AB = int(input("enter a no of much time add contact:"))
        for i in range(AB):
            A = input('enter a number:')
            B = input('enter a name:')
            contact[A]=B
            print("contact update")
    elif ch == 2:
        print("number\tname")
        for v,k in contact.items():
            print(v,'\t',k)
    elif ch == 3:
        D=input('update no.')
        
        if D in contact:
            H = input('enter a name:')
            contact[D]=H
    elif ch == 4:
        C=input('enter remove keys')
        contact.pop(C)
    elif ch == 5:
        print('exit')
    else:
        print('invalid choice')
        
    
