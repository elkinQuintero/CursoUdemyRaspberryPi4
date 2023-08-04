def suma(a,b):
    c = a+b
    return c
def resta(a,b):
    c = a-b
    return c
def algo(*args):
    for i in args:
        print(i)
def suma2(*args):
    total=0
    for i in args:
        total=total+i
    return total
def algo2(**kargs):
    print (kargs)

num1 = int(input("digite el numero 1: "))
num2 = int(input("digite el numero 2: "))
print("La suma es:",suma2(num1,num2,10,1))
print("La resta es:",resta(num1,num2))
algo("Roger",36,True)
algo2(nombre="Roger",edad=36,licencia=True)