import os

def add_contact():
    name = input("Informe o nome: \n")
    address = input("Informe o endereço: \n")
    phone = input("Informe o telefone: \n")

    contact = f"Nome: {name} \nEndereço: {address} \nTelefone: {phone} \n"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)
def view_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Nenhum contato encontrado.")
        return

    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Contatos:\n", contacts)

def delete_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Nenhum contato encontrado.")
        return
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("Todos os contatos foram deletados.")

    