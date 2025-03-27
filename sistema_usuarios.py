import sqlite3
import re

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criação da tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conexao.commit()

# Função para validar email
def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Função para adicionar usuário
def adicionar_usuario(nome, email):
    if not nome.strip():
        print("Erro: Nome não pode ser vazio!")
        return
    if not validar_email(email):
        print("Erro: Email inválido!")
        return
    try:
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já existe no banco de dados!")

# Função para listar usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
        print("-" * 50)

# Função para atualizar usuário
def atualizar_usuario(id_usuario, novo_nome, novo_email):
    if not novo_nome.strip():
        print("Erro: Nome não pode ser vazio!")
        return
    if not validar_email(novo_email):
        print("Erro: Email inválido!")
        return
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_usuario))
    if cursor.rowcount == 0:
        print("Erro: Usuário não encontrado!")
    else:
        conexao.commit()
        print("Usuário atualizado com sucesso!")

# Função para excluir usuário
def excluir_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    if cursor.rowcount == 0:
        print("Erro: Usuário não encontrado!")
    else:
        conexao.commit()
        print("Usuário excluído com sucesso!")

# Função para exibir o menu
def exibir_menu():
    print("\n=== Sistema de Gerenciamento de Usuários ===")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Excluir Usuário")
    print("5. Sair")
    return input("Escolha uma opção: ")

# Loop principal
while True:
    opcao = exibir_menu()

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        adicionar_usuario(nome, email)

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        listar_usuarios()
        try:
            id_usuario = int(input("ID do usuário a ser atualizado: "))
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            atualizar_usuario(id_usuario, novo_nome, novo_email)
        except ValueError:
            print("Erro: ID deve ser um número!")

    elif opcao == "4":
        listar_usuarios()
        try:
            id_usuario = int(input("ID do usuário a ser excluído: "))
            excluir_usuario(id_usuario)
        except ValueError:
            print("Erro: ID deve ser um número!")

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão
conexao.close()
print("Conexão com o banco de dados encerrada.")