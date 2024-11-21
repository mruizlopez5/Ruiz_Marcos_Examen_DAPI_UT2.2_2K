nombre = input("introduce tu nombre completo tal que Nombre Apellido1 Apellido2\n")
nombre = nombre.split(" ")
n = len(nombre)
for i in range(n):
    print(nombre[i].capitalize())