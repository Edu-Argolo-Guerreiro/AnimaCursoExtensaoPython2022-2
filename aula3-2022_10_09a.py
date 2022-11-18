contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1

# Laço for (python for = for each)
  
#Lista
frutas = ["morango", "laranja", "limão"]

#Quero exibir apenas limão
print(frutas[2])

#Exibir quantas frutas tem na minha lsita
print(len(frutas)) #length = tamanho
print(frutas)

#Quero incluir uma fruta nova
frutas.append("manga")
print(len(frutas))
print(frutas)

#i = numero
i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)


