#4.Desenvolva um cadastro de usuário que mantenha os dados: nome, e-mail e idade. USANDO CRUD

usuarios = []

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    idade = int(input("Digite a idade do usário: "))
    
    usuario = {"nome": nome, "email": email, "idade": idade}
    usuarios.append(usuario)
print("Usuários cadastrados. \n")

def listar_usuario():    
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Listar usuário: ")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

#NAO TERMINEI
