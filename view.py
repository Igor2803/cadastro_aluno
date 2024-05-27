# importando SQLite
import sqlite3 as lite 

#criando conexão
try: 
	con = lite.connect('cadastro_alunos.db')
	print('Conexao com o banco de dados realizada com sucesso')
except lite.Error as e: 
	print("Erro ao conectar com o banco de dados:" , e )


#Tabela de Cursos --------------

#Criar Cursos (CREATE C)
def criar_curso(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
		cur.execute(query,i)


#VER TODOS OS CURSO (READ R)
def ver_cursos():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Cursos')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista


#Atualizar os Cursos (Update U)
def atualizar_curso(i):
	with con:
		cur = con.cursor()
		query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
		cur.execute(query,i)


#Deletar os Cursos (Delete D)

def deletar_curso(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Cursos WHERE id=?"
		cur.execute(query,i)

#deletar_curso([1])



#Tabela de Turmas --------------

#Criar turmas ( Inserir )
def criar_turma(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Turmas (nome, curso_nome , data_inicio) VALUES (?, ?, ?)"
		cur.execute(query, i)


#Ver todas as turmas(Read R)
def ver_turmas():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Turmas')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista

#Atualizar as Turmas (Update U)
def atualizar_turma(i):
	with con:
		cur = con.cursor()
		query = "UPDATE Turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
		cur.execute(query,i)

#Deletar Turma (Delete D)
def deletar_turma(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Turmas WHERE id=?"
		cur.execute(query,i)



#Tabela Alunos --------------

#Criar Alunos ( Inserir )
def criar_alunos(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, tuma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
		cur.execute(query, i)


#Ver Alunos(Read R)
def ver_alunos():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Alunos')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista


#Atualizar as Alunos (Update U)
def atualizar_alunos(i):
	with con:
		cur = con.cursor()
		query = "UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, tuma_nome=? WHERE id=?"
		cur.execute(query,i)

#Deletar Aluno (Delete D)
def deletar_aluno(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Alunos WHERE id=?"
		cur.execute(query,i)

def procurar_aluno(i):
	with con:
		cur = con.cursor()
		query = "SELECT * FROM Alunos WHERE id=?"
		cur.execute(query,i)