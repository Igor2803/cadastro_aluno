#importantdo SqLite3
import sqlite3

#criando conexão
conn = sqlite3.connect('cadastro_alunos.db')
# definindo um cursor
cursor = conn.cursor()


    #criando tabela de de curso
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS Cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                duracao TEXT,
                preco REAL
                ) ;
                 """) 

print("Tabela cursos criado com sucesso")

    #criando tabela de turma
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                curso_nome TEXT,
                data_inicio DATE,
                FOREIGN KEY (curso_nome)  REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE 
                ) """) 

print("Tabela Turmas criado com sucesso")

   #criando tabela de alunos
   
cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone TEXT,
                sexo TEXT,
                imagem TEXT,
                data_nascimento DATE,
                cpf TEXT,
                tuma_nome TEXT,
                FOREIGN KEY (tuma_nome)  REFERENCES turmas (nome) ON DELETE CASCADE 
                ) """) 

print("Tabela alunos criado com sucesso")
