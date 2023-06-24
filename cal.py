def Add(num1,num2):
    return num1+num2
def Sub(num1,num2):
    return num1-num2
def Mul(num1,num2):
    return num1*num2
def Div(num1,num2):
    return num1/num2
def Mod_Div(num1,num2):
    return num1%num2
select=input("select one operation + ,- ,* ,/ ,% :")
num1=int(input("enter ur num1 value:"))
num2=int(input("enter ur num2 value:"))
if select=='+':
    print(num1," + ",num2," ","=",Add(num1,num2))
elif select=='-':
    print(num1," - ",num2," ","=",Sub(num1,num2))
elif select=='*':
    print(num1," * ",num2," ","=",Mul(num1,num2))
elif select=='/':
    print(num1," / ",num2," ","=",Div(num1,num2))
elif select=='%':
    print(num1," % ",num2," ","=",Mod_Div(num1,num2))
else:
    print("Invalid Input")