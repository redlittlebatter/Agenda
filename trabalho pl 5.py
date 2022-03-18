agenda = []

def nome_contato():
     return(input("Nome: "))

def telefone_contato():
     return(input("Telefone: "))

def email_contato():
    return(input("Email: "))

def twitter_contato():
    return(input("Twitter: "))

def instagram_contato():
    return(input("Instagram: "))

def compilado_dados(nome, telefone, email, instagram, twitter):
     print("Nome: %s, Telefone: %s, Email: %s, Twitter: %s, Instagram: %s." % (nome, telefone, email, twitter, instagram))
     
def apaga():
     global agenda
     nome = nome_contato()
     o = contato_interno(nome)
     if o != None:
          print("Contato deletado.")
          del agenda[o]
     else:
         print("Contato não encontrado.")
     
def novo():
     nome = nome_contato()
     telefone = telefone_contato()
     email = email_contato()
     twitter = twitter_contato()
     instagram = instagram_contato()
     agenda.append([nome, telefone, email, twitter, instagram])
     print("Contato cadastrado.")
     
               
def contato_interno(nome):
     qnome = nome.lower()
     for o, e in enumerate(agenda):
         if e[0].lower() == qnome:
               return o
     return None

          
def edicao():
     o = contato_interno(nome_contato())
     if o != None:
         nome = agenda[o][0]
         telefone = agenda[o][1]
         email = agenda[o][2]
         twitter = agenda[o][3]
         instagram = agenda[o][4]
         print("Contato encontrado.")
         compilado_dados(nome, telefone, email, instagram, twitter)
         print("Editar Contato:")
         nome = nome_contato()
         telefone = telefone_contato()
         email = email_contato()
         twitter = instagram_contato()
         instagram = twitter_contato()
         agenda[o] = [nome, telefone, email, twitter, instagram]
         print("Contato Editado.")
     else:
         print("Contato não encontrado.")

def lista():
     print("Agenda:")
     for e in agenda:
         compilado_dados(e[0], e[1], e[2], e[3], e[4])

def retorno_menu(opcao, inicio, fim):
     while True:
         try:
               numero = int(input(opcao))
               if inicio <= numero <= fim:
                   return(numero)
         except ValueError:
               print("Opção inválida, favor digitar uma opção válida entre %d e %d." % (inicio, fim))

def achar():
     global agenda
     nome = input("Digite o nome do contato a ser exibido: ")
     for e in agenda:
            if nome == e[0]:
                print("Nome:",e[0],",","Telefone:",e[1],",","Email:", e[2],",","Twitter:", e[3],",","Instagram:", e[4],".")
            else:
                print("Contato não encontrado.")
               

def simultaneo():
     option2 = int(input("Gostaria de adicionar quantos?"))
     while option2 >= 1:
          nome = nome_contato()
          telefone = telefone_contato()
          email = email_contato()
          twitter = twitter_contato()
          instagram = instagram_contato()
          agenda.append([nome, telefone, email, twitter, instagram])
          print("Contato cadastrado.")
     else:
          print("Número inválido, por favor digite um número válido.")
                    
           
     
                
def menu():
     
     print("""
   1 - Novo Contato
   2 - Editar Contato
   3 - Remover Contato
   4 - Lista de Contatos
   5 - Vizualizar Contato
   6 - Adicionar Vários Contatos 
   0 - Sair
""")
     return retorno_menu("Escolha uma opção: ",0,6)

while True:
     opcao = menu()
     if opcao == 0:
         break
     elif opcao == 1:
         novo()
     elif opcao == 2:
         edicao()
     elif opcao == 3:
         apaga()
     elif opcao == 4:
         lista()
     elif opcao == 5:
         achar()
     elif opcao == 6:
          simultaneo()
