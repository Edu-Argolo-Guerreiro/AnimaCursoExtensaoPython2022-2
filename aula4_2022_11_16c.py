#1° passo: importar a biblioteca sqlite3
import sqlite3

#Passos (2 e 3) virarão função conectar()
def conectar():
  
  #2° passo: vamos estabeler uma conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #3° passo: criar um objeto tipo cursor
  cursor = conexao.cursor()
  return conexao, cursor