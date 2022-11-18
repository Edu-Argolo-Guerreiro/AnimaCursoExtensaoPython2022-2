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

valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print(f"O imposto de 5% {valor} é {calc_imposto(valor)}")

#Declarar uma função calc_imposto_aliquota que recebe dois parânmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Ser a alíquota não for informada, utilize 7% como padrão.
def calc_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de 7% de {valor} é {calc_imposto_aliquota(valor)}")
 