import tkinter as tk
from tkinter import ttk

def enviar():
    print("----- Dados do Cliente -----")
    print("Nome:", entry_nome.get())
    print("Idade:", entry_idade.get())
    print("E-mail:", entry_email.get())
    print("Endereço:", entry_endereco.get())
    print("Celular:", entry_celular.get())
    print("CEP:", entry_cep.get())
    print("Cidade:", entry_cidade.get())
    print("Cursos:", entry_cursos.get())
    print("-----------------------------\n")

# Janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("1700x750")

# Frame principal
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Permitir que a coluna 1 cresça proporcionalmente
frame.columnconfigure(1, weight=1)

# Campos do formulário
tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame, font=("Island Moments", 14))
entry_nome.grid(row=0, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Idade:").grid(row=1, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame, font=("Island Moments", 14))
entry_idade.grid(row=1, column=1, pady=5, sticky="ew")

tk.Label(frame, text="E-mail:").grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame, font=("Island Moments", 14))
entry_email.grid(row=2, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Endereço:").grid(row=3, column=0, sticky="w", pady=5)
entry_endereco = tk.Entry(frame, font=("Island Moments", 14))
entry_endereco.grid(row=3, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Celular:").grid(row=4, column=0, sticky="w", pady=5)
entry_celular = tk.Entry(frame, font=("Island Moments", 14))
entry_celular.grid(row=4, column=1, pady=5, sticky="ew")

tk.Label(frame, text="CEP:").grid(row=5, column=0, sticky="w", pady=5)
entry_cep = tk.Entry(frame, font=("Island Moments", 14))
entry_cep.grid(row=5, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Cidade:").grid(row=6, column=0, sticky="w", pady=5)
entry_cidade = tk.Entry(frame, font=("Island Moments", 14))
entry_cidade.grid(row=6, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Cursos:").grid(row=7, column=0, sticky="w", pady=5)
entry_cursos = tk.Entry(frame, font=("Island Moments", 14))
entry_cursos.grid(row=7, column=1, pady=5, sticky="ew")

# Botão Enviar
btn_enviar = tk.Button(frame, text="Enviar", command=enviar, width=20, bg="#4CAF50", fg="white", font=("Island Moments", 14))
btn_enviar.grid(row=9, column=1, pady=20, sticky="e")

root.mainloop()



# import sqlite3
# import tkinter as tk
# from tkinter import messagebox


# def conexao():
#     return sqlite3.connect('banco_teste.db')

# def criar_tabela():
#     conn = conexao()
#     cursor = conn.cursor()
#     cursor.execute(''' CREATE TABLE IF NOT EXISTS dados(
                   
#                    nome TEXT,
#                    email TEXT
                   
#                    )''')
#     conn.commit()
#     conn.close()


# def inserir():
#     conn = conexao()
#     cursor = conn.cursor()
#     nome_ =nome.get()
#     email_ = email.get() 

#     if nome_ and email_: 
    
#        cursor.execute('INSERT INTO dados VALUES(?,?)',(nome_, email_))
#        conn.commit()
#        conn.close()
#        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')
#     else:
#         messagebox.showerror('', 'DECLARE TODOS OS DADOS!')   




# janela =  tk.Tk()


# tk.Label(janela, text='nome: ').pack()

# nome = tk.Entry(janela)
# nome.pack()

# tk.Label(janela, text='e-mail: ').pack()

# email = tk.Entry(janela)
# email.pack()


# btn =  tk.Button(janela, text='inserir no banco', command=inserir)
# btn.pack()



# criar_tabela()

# janela.mainloop()

# https://www.sqlite.org/famous.html

# import sqlite3


# conn  = sqlite3.connect('meu_banco.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
                
#                 nome TEXT,
#                 email TEXT,
#                 idade TEXT
                
               
#                )''')
# conn.commit()


# nome  =  input('nome: ')
# idade  =  input('idade: ')
# email = input('e-mail:')


# cursor.execute('INSERT INTO dados VALUES(?,?,?)', (nome, email,idade))
# conn.commit()


# cursor.execute('SELECT * FROM dados')
# dados  =  cursor.fetchall()
# print(dados)



# conn.close()