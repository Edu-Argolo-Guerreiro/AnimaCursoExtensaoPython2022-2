#1° passo: importar a biblioteca sqlite3
import sqlite3

#2° passo: vamos estabeler uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar um objeto tipo cursor
cursor = conexao.cursor()

#4° passo: Cursando SQL no banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5° passo: Executar o comando SQL no SQLlite (no cursor)
cursor.execute(sql)

#6° passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
for pessoa in pessoas:
  print(f"nome:{pessoa[1]} ({pessoa[3]})")