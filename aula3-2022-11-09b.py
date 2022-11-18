#criação de funções

preco = 1999.90

#calcular 5% de imposto, guardar na variavel imposto e exibir na tela.
imposto = preco * 0.05
print(imposto)

#criar uma função calc_imposto() que calcula um imposto de 5% e retorna a quem pediu...
def calc_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... é imposto a calcular e exibir na tela
preco = 299
imposto = calc_imposto(preco)
print(imposto)