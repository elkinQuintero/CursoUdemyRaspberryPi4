lista = []
tupla = ()
dicc = {"nombre":"roger","edad":36,"notas":{"fisica":17,"quimica":13,"matematica":16}}
print(type(dicc))
dicc["licencia"]=True
a = dicc.items()
for i in a:
    print(i[1])