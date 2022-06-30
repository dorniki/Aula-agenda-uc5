from classe_agenda import *

class Menu:
    def __init__(self):
        agenda_davi= Agenda() 

 ##iniciar menu
        while True:  
            entrada = input('informe a opção desajada'
                            '\n1 - novo contato'
                            '\n2 - listar contatos'
                            '\n3 - Alterar telefone'
                            '\n0 - sair\n')

            if entrada == '1':
                agenda_davi.salvar_contatos()
            elif entrada == '2':
                agenda_davi.listar_todos_contatos()
            elif entrada == '3':
                agenda_davi.alterar_telefone()
            elif entrada == '0':
                break
            else:
                print('opção errada!')                                
