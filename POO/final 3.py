from Contact import Contact
from Contactbook import ContactBook

# Criando a agenda
book = ContactBook()

# Adicionando alguns contatos
book.add_contact(Contact("Ana", "1111-1111", "ana@email.com"))
book.add_contact(Contact("João", "2222-2222", "joao@email.com"))

def menu():
    print("Bem-vindo à sua agenda\n")
    while True:
        escolha = int(input(
            "O que deseja fazer?\n"
            "1 - Adicionar contatos\n"
            "2 - Listar contatos\n"
            "3 - Buscar contatos\n"
            "4 - Remover contatos\n"
            "5 - Sair\n"
            "Escolha: "
        ))

        if escolha == 1:
            name = input("Nome: ")
            phone = input("Telefone: ")
            email = input("Email: ")
            book.add_contact(Contact(name, phone, email))

        elif escolha == 2:
            book.list_contacts()

        elif escolha == 3:
            term = input("Digite o termo de busca (nome/telefone/email): ")
            book.search_contacts(term)

        elif escolha == 4:
            email = input("Digite o email do contato a remover: ")
            book.remove_contact(email)

        elif escolha == 5:
            print("Até mais!")
            break

        else:
            print("Escolha inválida. Tente novamente.")

menu()