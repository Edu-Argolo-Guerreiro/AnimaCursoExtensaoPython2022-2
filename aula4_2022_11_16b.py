#1° passo: importar a biblioteca sqlite3
import sqlite3

#2° passo: vamos estabeler uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar um objeto tipo cursor
cursor = conexao.cursor()

#4° passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'Wolverine', 'Logan', 'Herói(na)')"

#5° passo: Executar o comando SQL
cursor.execute(sql)

#6° passo: confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()