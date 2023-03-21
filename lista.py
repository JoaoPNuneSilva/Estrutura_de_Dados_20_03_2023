import os
os.system("cls") #Limpa o terminal

lista1 = ["Informática", "Medicina", "Engenharia"]

print(type(lista1))

lista1.append("Bomedicina") #para inserir um valor

lista1.remove("Informática")

for litageral in lista1:
    print(litageral)