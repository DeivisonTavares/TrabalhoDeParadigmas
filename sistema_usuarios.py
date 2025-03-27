import sqlite3

# Criar conexão com o banco de dados SQLite
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criar tabela de usuários (caso não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conexao.commit()

# Função para adicionar usuário
def adicionar_usuario(nome, email):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    print("Usuário adicionado com sucesso!")

# Função para listar usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print("\nLista de Usuários:")
    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
    print("-" * 30)

# Função para atualizar usuário
def atualizar_usuario(id_usuario, novo_nome, novo_email):
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_usuario))
    conexao.commit()
    print("Usuário atualizado com sucesso!")

# Função para excluir usuário
def excluir_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    print("Usuário excluído com sucesso!")

# Menu interativo
while True:
    print("\n1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Excluir Usuário")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        adicionar_usuario(nome, email)

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        listar_usuarios()
        id_usuario = int(input("ID do usuário a ser atualizado: "))
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo email: ")
        atualizar_usuario(id_usuario, novo_nome, novo_email)

    elif opcao == "4":
        listar_usuarios()
        id_usuario = int(input("ID do usuário a ser excluído: "))
        excluir_usuario(id_usuario)

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
conexao.close()
print("Conexão com o banco de dados encerrada.")