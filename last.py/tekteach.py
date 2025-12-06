import tkinter as tk


def display():
    nome  =  nome_input.get()
    idade =  idade_input.get()
    email = email_input.get()
    endereco = endereco_input.get()
    cep = cep_input.get()
    curso = curso_input.get()
    celular = celular_input.get()
    cidade  =  cidade_input.get()

    print(f'''
        nome: {nome}
        idade: {idade}
        e - mail : {email}
        endereço:{endereco}
        cep: {cep}  
        curso:{curso}
        celular:{celular}
        cidade: {cidade}


     ''')  


root =  customtkinter.CTk()
root.configure(fg_color='#DCDCDC')
root.title('FORMULARIO')

customtkinter.CTkLabel(root, text = 'FORMULÁRIO DE DADOS ', font=('Montserrat', 12)).grid(row = 0, column =  0)


nome_texto   =  customtkinter.CTkLabel(root, text = 'Nome: ', font=('Montserrat', 12))
nome_texto.grid(row = 1, column = 0)

nome_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
nome_input.grid(row = 1 , column = 1)


idade_texto   =  customtkinter.CTkLabel(root, text = 'idade: ', font=('Montserrat', 12))
idade_texto.grid(row = 2, column = 0)

idade_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
idade_input.grid(row = 2 , column = 1)



email_texto   =  customtkinter.CTkLabel(root, text = 'email: ', font=('Montserrat', 12))
email_texto.grid(row = 3, column = 0)

email_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
email_input.grid(row = 3 , column = 1)


# email_texto   =  customtkinter.CTkLabel(root, text = 'email: ', font=('Montserrat', 12))
# email_texto.grid(row = 4, column = 0)

# email_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
# email_input.grid(row = 4 , column = 1)


cep_texto   =  customtkinter.CTkLabel(root, text = 'cep: ', font=('Montserrat', 12))
cep_texto.grid(row = 5, column = 0)

cep_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
cep_input.grid(row = 5 , column = 1)


celular_texto   =  customtkinter.CTkLabel(root, text = 'celular: ', font=('Montserrat', 12))
celular_texto.grid(row = 6, column = 0)

celular_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
celular_input.grid(row = 6 , column = 1)



endereco_texto   =  customtkinter.CTkLabel(root, text = 'endereço: ', font=('Montserrat', 12))
endereco_texto.grid(row = 7, column = 0)

endereco_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
endereco_input.grid(row = 7 , column = 1)


cidade_texto   =  customtkinter.CTkLabel(root, text = 'cidade: ', font=('Montserrat', 12))
cidade_texto.grid(row = 8, column = 0)

cidade_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
cidade_input.grid(row = 8, column = 1)


curso_texto   =  customtkinter.CTkLabel(root, text = 'curso: ', font=('Montserrat', 12))
curso_texto.grid(row = 9, column = 0)

curso_input = customtkinter.CTkEntry(root, font=('Montserrat', 12))
curso_input.grid(row = 9 , column = 1)

btn =  customtkinter.CTkButton(root, font=('Montserrat', 12), command=display)
btn.grid(row = 10 , column = 1)


root.mainloop()