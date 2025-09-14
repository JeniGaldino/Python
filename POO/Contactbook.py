from Contact import Contact  # importa a classe Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contato adicionado com sucesso!")

    def list_contacts(self):
        if not self.contacts:
            print("Agenda vazia.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i} - {contact}")

    def search_contacts(self, term):
        print(f"Resultados da busca por '{term}':")
        found = False
        for contact in self.contacts:
            if term.lower() in contact.name.lower() or \
               term.lower() in contact.phone.lower() or \
               term.lower() in contact.email.lower():
                print(contact)
                found = True
        if not found:
            print("Nenhum contato encontrado.")

    def remove_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                print("Contato removido com sucesso!")
                return
        print("Contato não encontrado.")
