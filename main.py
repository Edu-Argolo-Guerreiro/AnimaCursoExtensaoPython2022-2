# Meu primeiro projeto Python!!!
# (#) serve para comentario
# print () = comando de saida
#String = letras, nomes, alfas numeros (frase).
#Int/Boolean = sem aspas (variavel inteira)
print("Hello World")

nome = "Edu Guerreiro"
idade = 18

print(nome)
print(idade)

#Quando quiser exibir a frase minha "minha idade é:" completando com o conteúdo idade. (Usasse +)
#Para fazer uma variavel inteira virar string, usasse(+str())

print("Minha idade é:"+str(idade)+"anos")
print(f"Minha idade é:{idade}\n anos")
print("Minha idade é:{} anos".format(idade))

#Quando quiser exibir nome e idade pelas variaveis, usasse:
print("Meu nome é {} e tenho {} anos".format(nome,idade))



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
