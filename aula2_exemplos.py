nome = input("Qual o seu nome: ")
idade = int(input("Qual sua idade: "))
nota = float(input("Qual sua nota: "))
#Float serve para decimais também!

if (nota == 10):
  print("{}, voce é o bixão mesmo".format(nome))
elif(nota >= 6 and nota <=9.9):
#elif = meio termo de if and else
  print("{}, parabéns, voce é mediano".format(nome))
else: #é automaticamente o que as condições de cima não trataram
  print("{}, burrão fi...".format(nome))

#Exemplo de laço

#E se eu quisesse exibir números de 1 a 10?
numero = 1
print ("{}".format(numero))
numero += 1
print ("{}".format(numero))
