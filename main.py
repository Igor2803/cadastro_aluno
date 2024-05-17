# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# importando pillow
from PIL import ImageTk, Image

#tk calendario
from tkcalendar import Calendar, DateEntry
from datetime import date

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


#Trabalhando no frame Logo -----------
app_lg = Image.open('logo.png')
app_lg = app_lg.resize((60,60))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos 'Instituto Bueno'", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)


#Funcao para cadastrar alunos
def alunos():
   
    #criando campos de entrada
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome= Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

    l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email= Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_email.place(x=7, y=100)

    l_tel = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_tel.place(x=4, y=130)
    e_tel= Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_tel.place(x=7, y=160)

    #selecao de sexo
    l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_sexo.place(x=190, y=130)
    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8'))
    c_sexo['values'] = ('Masculino', 'Feminino')
    c_sexo.place(x=190, y=160)

    l_data_nascimento = Label(frame_detalhes, text="Data de Nascimento *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_nascimento.place(x=467, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, background='darkblue', foreground='white', borderwidth=2, year=2024)
    data_nascimento.place(x=467, y=40)

    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_cpf.place(x=467, y=70)
    e_cpf= Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=467, y=100)

    #Pegando as Turmas
    turmas = ['Turma A', 'Turma B']
    turma = []

    for i in turmas:
       turma.append(i)

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_turma.place(x=467, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8'))
    c_turma['values'] = (turma)
    c_turma.place(x=467, y=160)

#Funcao para adicionar Cursos e Turmas
def adicionar():
    #criado frames para tabelas ---------------------
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)


#Detalhes Curso -------------------------


    l_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao= Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_preco.place(x=4, y=140)
    e_preco= Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)
    
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=197, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=287, y=160)


#Tabela Cursos
    def mostrar_cursos():
     app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
     app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

     #creating a treeview with dual scrollbars
    list_header = ['ID','Curso','Duração','Preço']

    df_list = []

    global tree_curso

    tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

    tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree_curso.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_curso.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","e","e"]
    h=[90,150,80,60]
    n=0

    for col in list_header:
     tree_curso.heading(col, text=col.title(), anchor=NW)
    #adjust the column's width to the header string
     tree_curso.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in df_list:
     tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

    # linha separatoria --------
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=394, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=392, y=10)



     # linha separatoria  tabela--------
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=7, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=5, y=10)



    #Detalhes Turma -------------------------
    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_nome.place(x=424, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_turma.place(x=427, y=40)

    l_turma = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Ivy 10' ), bg=co1, fg=co4)
    l_turma.place(x=424, y=70)
    
    #Pegando os cursos
    cursos = ['curso1', 'curso 2']
    curso = []

    for i in cursos:
       curso.append(i)

    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8'))
    c_curso['values'] = (curso)
    c_curso.place(x=427, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=427, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidth=2, year=2024)
    data_inicio.place(x=427, y=160)


    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=530, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=620, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=710, y=160)


    #Tabela Turmas
    def mostrar_turmas():
     app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
     app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

     #creating a treeview with dual scrollbars
    list_header = ['ID','Turma','Curso','Inicio']

    df_list = []

    global tree_turma

    tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

    tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree_turma.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_turma.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","e","e"]
    h=[90,150,80,60]
    n=0

    for col in list_header:
     tree_turma.heading(col, text=col.title(), anchor=NW)
    #adjust the column's width to the header string
     tree_turma.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in df_list:
     tree_turma.insert('', 'end', values=item)

    mostrar_turmas()








#Funcao para salvar
def salvar():
    print('Salvar')



# Funcao de control --------------------------------------------

def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy() 

        for widget in frame_tabela.winfo_children():
            widget.destroy() 
        
        # chamando a funcao alunos
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy() 

        for widget in frame_tabela.winfo_children():
            widget.destroy() 
        
        # chamando a funcao adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy() 

        for widget in frame_tabela.winfo_children():
            widget.destroy() 
        
        # chamando a funcao salvar
        salvar()







# criando botoes --------------


app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button (frame_dados,command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11 '), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)



app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button (frame_dados,command=lambda:control('adicionar'), image=app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11 '), bg=co1, fg=co0)
app_adicionar.place(x=143, y=30)


app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button (frame_dados,command=lambda:control('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11 '), bg=co1, fg=co0)
app_salvar.place(x=276, y=30)



# Executando a janela
alunos()
janela.mainloop()
