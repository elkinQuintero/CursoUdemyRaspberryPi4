class Operaciones:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
        self.otro = "Soy variable de la clase"
    def suma(self):
        c = self.num1+self.num2
        return c
    def resta(self):
        c = self.num1-self.num2
        return c
    def multi(self):
        c = self.num1 * self.num2
        return c
    def divi(self):
        c = self.num1 / self.num2
        return c
print("Inicio del programa principal")
continuar = True
op = Operaciones(3,4)
while continuar:
    dato1 = input("digite el numero1: ")
    dato2 = input("digite el numero2: ")
    if dato2 == "z":
        continuar = False
    else:
        op.num1 = int(dato1)
        op.num2 = int(dato2)
        print("La suma es:",op.suma())
        print("La resta es:",op.resta())
        print("La multiplicacion es:",op.multi())
        print("La division es:",op.divi())
        print(op.otro)
print("Fin del programa principal")