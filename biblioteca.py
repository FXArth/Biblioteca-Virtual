"""
- Artigos/Livros/Documentários
    - Id
    - Nome
    - Ano de publicacao
    - Autor
    - Edição

- Usuários
    - Id
    - Nome
    - CPF
    - Email
    - Senha
    - Histórico

- Leitor
    - Id
    - Nome
    - CPF
    - Email
    - Senha

- Administrador
    - Id
    - Nome
    - CPF
    - Cargo/Nível de acesso
    - Email
    - Senha

        # id = ""                                         #identificação para rastreamento
        # nome = ""                                       #nome do livro
        # tipo = ""                                       #artigo, livro ou documentário
        # autor = ""                                      #nome do autor no livro
        # status = ""                                     #disponível ou ou indisponível para aluguel
        # ano_de_publicacao = ""                          #ano de publicação do conteúdo
"""

from datetime import date
import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS biblioteca (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                autor TEXT NOT NULL,
                status TEXT NOT NULL,
                ano_de_publicação INTEGER NOT NULL,
                edicao INTEGER NOT NULL
                )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS historico (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    livros_alugados TEXT,
                    tempo_de_aluguel INTEGER,
                    reputação TEXT NOT NULL
                )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS leitores (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL
                )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS administradores (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    cargo TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL
                )""")


class Material:

    def __init__(self, nome, autor, ano_de_publicacao, status):
        self.nome = nome
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.status = status


class Usuario:

    def __init__(self, id, nome, cpf, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Administrador:

    def __init__(self, id, nome, cpf, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email


class TelaInicial:
    def apresentacao(self):
        print("-" * 40)
        print("Bem-vindo ao Sistema Bibliotecário!")
        print("1 - Fazer Login")
        print("2 - Cadastrar Leitor")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            self.sub_menu_login()
        elif opcao == "2":
            self.sub_menu_cadastro()

    def sub_menu_cadastro(self):
        print("""--Cadastro--
Você deseja se cadastrar como:

1 - Usuário
2 - Administrador
""")
        try:
            tipo_cadastro = input()

            if tipo_cadastro == "1":
                self.cadastrar_leitor()
            elif tipo_cadastro == "2":
                self.cadastrar_administrador()
        except Exception as error:
            print(error)

    def cadastrar_leitor(self):

        print("-" * 40)
        print(
            "--Cadastro--\n\nPor Gentileza! Insira as informações solicitadas à seguir!"
        )
        nome = input("Me diga seu nome: ")
        cpf = input("Qual seu CPF?: ")
        email = input("Para contato, nos diga seu email: ")
        senha = input("Crie agora, sua senha: ")

        cursor.execute(
            """
            INSERT INTO leitores (nome, cpf, email, senha) VALUES (?, ?, ?, ?)""",
            (nome.title().strip(), cpf.upper().strip(), email.lower().strip(), senha),
        )

        conexao.commit()
        print("Seu cadastro foi realizado!")

    def cadastrar_administrador(self):

        print("-" * 40)
        print(
            "--Cadastro--\n\nPor Gentileza! Insira as informações solicitadas à seguir!"
        )
        nome = input("Me diga seu nome: ")
        cpf = input("Qual seu CPF?: ")
        email = input("Para contato, nos diga seu email: ")
        senha = input("Crie agora, sua senha: ")

        cursor.execute(
            """
            INSERT INTO administradores (nome, cpf, email, senha) VALUES (?, ?, ?, ?)""",
            (nome.title().strip(), cpf.upper().strip(), email.lower().strip(), senha),
        )

        conexao.commit()
        print("Seu cadastro foi realizado!")

    def sub_menu_login(self):
        print("""--Login--
    Você deseja fazer login como:
    
    1 - Usuário
    2 - Administrador
    """)

        tipo_login = input()

        if tipo_login == "1":
            self.login_leitor()
        elif tipo_login == "2":
            self.login_administrador()

    def login_leitor(self):
        print("-" * 40)
        print(
            "--Login--\n\nBom te ver de novo! Insira as informações solicitadas à seguir!"
        )

        nome = input("Nome: ")
        senha = input("Senha: ")

        cursor.execute(
            "SELECT * FROM leitores WHERE nome = ? AND senha = ?",
            (nome.title().strip(), senha),
        )

        resultado = cursor.fetchone()

        if resultado:
            print("\nLogin realizado! Bem-vindo de volta.")

            # 1. Criamos a "Entidade" do usuário logado
            usuario_logado = Usuario(
                resultado[0], resultado[1], resultado[2], resultado[3]
            )

            # 2. Ligamos o motor do Sistema e abrimos a porta para esse usuário
            sistema = Sistema()
            sistema.menu_usuario(usuario_logado)

        else:
            print("\nNome ou senha incorretos! Tente novamente.")

    def login_administrador(self):

        print("-" * 40)
        print(
            "--Login--\n\nBom te ver de novo! Insira as informações solicitadas à seguir!"
        )

        nome = input("Nome: ")
        senha = input("Senha: ")

        cursor.execute(
            "SELECT * FROM administradores WHERE nome = ? AND senha = ?",
            (nome.title().strip(), senha),
        )

        resultado = cursor.fetchone()

        if resultado:
            print("\nLogin realizado! Bem-vindo de volta.")

            # 1. Criamos a "Entidade" do usuário logado
            administrador_logado = Administrador(
                resultado[0], resultado[1], resultado[2], resultado[3]
            )

            # 2. Ligamos o motor do Sistema e abrimos a porta para esse usuário
            sistema = SistemaAdministrador()
            sistema.menu_adm(administrador_logado)

        else:
            print("\nNome ou senha incorretos! Tente novamente.")


class Sistema:

    def menu_usuario(self, usuario):
        try:
            print("-" * 40)
            print("--Biblioteca virtual iniciada--")
            print(f"\nOlá {usuario.nome}! Seja bem vindo!")
            print("O que deseja?\n")
            print("""1 - Encontrar Material
2 - Devolver Material
3 - Histórico
4 - Sair\n""")

            acao = int(input("Selecione apenas o número da opção desejada: "))

            if acao == 1:
                self.busca()
            elif acao == 2:
                self.devolucao()
            elif acao == 3:
                historico = Historico(usuario.nome)
                historico.procurar()

            elif acao == 4:
                print("Saindo...")

        except Exception as error:
            print(f"Erro ocorrido: {error}")

    def busca(self):

        print("\n--- Buscar Livro ---")
        termo_busca = input("Digite o nome do livro que deseja procurar: ")

        cursor.execute(
            "SELECT * FROM biblioteca WHERE nome LIKE ?", ("%" + termo_busca + "%",)
        )

        resultados = cursor.fetchall()

        if resultados:

            print("\nEncontramos o(s) seguinte(s) livro(s):")

            for item in resultados:

                print(
                    f"ID: {item[0]} | Título: {item[1]} | Autor: {item[3]} | Status: {item[4]}"
                )

                if item[4] != "Disponível":
                    print(
                        f"Infelizmente o Material de título: '{item[1]}' não está disponível para aluguel. Talvez tenhamos outros títulos que goste! Continue buscando!"
                    )
                else:
                    print("Você deseja alugar esse(s) título(s)?")
                    aluguel = input("(S/N)  ")

                    if aluguel.upper().strip() != "S":
                        print(
                            "Tudo bem, talvez tenhamos outros títulos que goste! Continue buscando!"
                        )
                    else:
                        self.emprestimo(item[1])
        else:
            print("\nNenhum livro encontrado com esse nome.")

    def emprestimo(self, nome_livro):

        try:

            print("\n\n--Aba de Empréstimos--\n")
            data = int(
                input(
                    "Digite a quantidade de dias que pretende ficar com o livro (**limite de 90 dias**): "
                )
            )

            if data <= 90:
                cursor.execute(
                    "UPDATE biblioteca SET status = 'Indisponível' WHERE nome = ?",
                    (nome_livro,),
                )
                conexao.commit()
                print(
                    f"O seu prazo de {data} dias será contado a partir de amanhã. Aproveite sua leitura!"
                )
            else:
                print("Esse período ultrapassa o limite! Execução cancelada!")

        except Exception as erro:
            print("Utilize um dado válido (número).")
            print(f"Erro ocorrido {erro}")

    def devolucao(self):

        try:
            print("\n\n--Aba de Devoluções--\n")
            livro_devolucao = input(
                "Olá! Vejo que você quer devolver um livro. Qual o nome dele?: "
            )

            cursor.execute(
                "SELECT * FROM biblioteca WHERE nome LIKE ?",
                ("%" + livro_devolucao + "%",),
            )
            resultado = cursor.fetchone()

            if resultado:

                status_atual = resultado[4]

                if status_atual == "Indisponível":
                    print(
                        f"\nTem certeza que deseja devolver do título: '{resultado[1]}' do(a) Autor(a): {resultado[3]}"
                    )
                    confirmacao = input("(S/N): ").strip().upper()
                    if confirmacao == "S":
                        cursor.execute(
                            "UPDATE biblioteca SET status = 'Disponível' WHERE nome LIKE ?",
                            (livro_devolucao,),
                        )
                        conexao.commit()
                        print(
                            "\nDevolução realizada com sucesso! O material já está disponível para novos leitores."
                        )
                    else:
                        print("Devolução cancelada.")
                else:
                    print(
                        f"\nO livro '{resultado[1]}' já consta como 'Disponível' no nosso sistema. Não há devolução pendente."
                    )
            else:
                print(
                    "\nLivro não encontrado no banco de dados. Verifique se o nome foi digitado corretamente."
                )

        except Exception as erro:
            print("Utilize um dado válido (nome do Livro).")
            print(f"Erro ocorrido {erro}")


class SistemaAdministrador(Sistema):

    def menu_adm(self, administrador):

        print("-" * 40)
        print("--Biblioteca virtual iniciada--")
        print(
            f"\nOlá {administrador.nome}! Seja bem vindo ao ambiente de administração!"
        )
        print("O que deseja?")
        print("""1 - Postar Material
    2 - Deletar Material
    3 - Encontrar Material
    4 - Sair""")

        acao = int(input("Selecione a opção desejada: "))
        if acao == 1:
            self.adicionar_material()
        elif acao == 2:
            self.deletar_material()
        elif acao == 3:
            self.busca()
        elif acao == 4:
            print("Saindo...")

    def adicionar_material(self):

        try:

            print("Preencha as informações do livro")

            nome = input("Nome: ")
            tipo = input("Tipo (Artigo, Livro ou Documentario): ")
            autor = input("Autor: ")
            ano_de_publicacao = input("Ano_de_publicação: ")
            edicao = input("Edicao: ")
            status = "Disponível"

            criar_livro = input(
                "\nVocê deseja continuar com a criação desse livro?\nS/N:  "
            )

            if criar_livro.strip().upper() != "S":
                print("LIvro não adicionado! Excluindo informações!".upper())
            else:
                cursor.execute(
                    """
                INSERT INTO biblioteca (nome, tipo, autor, status, ano_de_publicação, edicao)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                    (
                        nome.title().strip(),
                        tipo.title().strip(),
                        autor.title().strip(),
                        status.title().strip(),
                        ano_de_publicacao.title().strip(),
                        edicao.title().strip(),
                    ),
                )
                conexao.commit()

                print("\nLivro salvo no banco de dados com sucesso!")

                novo_material = Material(
                    nome.title(),
                    autor.title(),
                    ano_de_publicacao.title(),
                    edicao.title(),
                    status.title(),
                )
                return novo_material

        except Exception as erro:
            print(f"Deu este erro: {erro}")

    def deletar_material(self):

        try:

            print("--Deletar Material--")

            delecao = input("Qual o nome do Material a ser deletado?: ").strip()
            cursor.execute("DELETE FROM biblioteca WHERE nome = ?", (delecao,))

            if cursor.rowcount > 0:
                conexao.commit()
                print(f"\n O Material com nome de: {delecao} foi deletado com sucesso!")
            else:
                print(
                    f"\n Não foi encontrado nenhum Material com o nome '{delecao}' para ser deletado"
                )

        except sqlite3.Error as erro_banco:
            print(f"Erro ao acessar o banco de dados: {erro_banco}")
        except Exception as error:
            print(f"Ocorreu um erro: {error}")


class Historico:

    def __init__(self, usuario):
        self.usuario = usuario

    def procurar(self):

        cursor.execute("SELECT * FROM historico WHERE nome = ?", (self.usuario,))
        print(cursor.fetchall())


class HistoricoAdministrador:

    def procurar(self):

        cursor.execute("SELECT * FROM historico WHERE nome = ?", (self.user_admin,))
        print(cursor.fetchall())


app = TelaInicial()
app.apresentacao()
