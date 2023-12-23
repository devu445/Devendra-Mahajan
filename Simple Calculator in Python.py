


class Arith:
    def ADD(self):
        A=int(input('enter A no:'))
        B=int(input('enter B no:'))
        Ans = A + B
        return f'ans={Ans}'

    def SUB(self):
        A=int(input('enter A no:'))
        B=int(input('enter B no:'))
        Ans = A - B
        return f'ans={Ans}'

    def MUL(self):
        A=int(input('enter A no:'))
        B=int(input('enter B no:'))
        Ans = A * B
        return f'ans={Ans}'

    def DIV(self):
        A=int(input('enter A no:'))
        B=int(input('enter B no:'))
        Ans = A / B
        return f'ans={Ans}'
    
        
    
myobj=Arith()
while True:
    Ch=int(input('1.ADD\t2.SUB\n3.MUL\t4.DIV'))
    if Ch==1:
        print(myobj.ADD())
    elif Ch==2:
        print(myobj.SUB())
    elif Ch == 3:
        print(myobj.MUL())
    elif Ch==4:
        print(myobj.DIV())
