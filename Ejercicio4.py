ent = int(input("introduce numero entero: "))
lista = []
lista2 = []
for i in range(3,ent+1,3):
    lista.append(i)
    if i%5 == 0:
        lista2.append(i)

print(lista)
print(lista2)