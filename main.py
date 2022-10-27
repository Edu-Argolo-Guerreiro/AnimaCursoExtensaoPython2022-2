#Comando input(): quero permitir que o usuario digite algo...
nome = input("Digite seu nome: ")

#Comando de saída... exibir na tela
print(f"Boa noite, talvez seu nome seja {nome}")

idade = int(input("Digite sua idade: "))

print("Sua idade é: {} anos".format(idade))

print("{} você tem atualmente {} anos".format(nome,idade))

#E se eu quisesse mostrar o dobro da idade informada? Preciso colocar o (int)
dobro = idade * 2

print("O dobro da sua idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "Se" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
#Else é o ao contrario de if "se não"
else:
  print("Você é menor de idade, só poder comer terra!")

#E se eu quisesse perguntar o gênero (M = Masculino e F = feminino)
#Mostre (...e você também precisa/precisou prestar serviço militar obrigatório)
genero = input("Informe o gênero M= Masculino, F= Feminino, O= Outros: ")

if idade >= 18 and genero == "M":
  print("e você também precisa/precisou prestar serviço militar obrigatório")


print("vai ser executada de qualquer jeito")
