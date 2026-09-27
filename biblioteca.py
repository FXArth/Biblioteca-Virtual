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
                livros_alugados TEXT NOT NULL,
                tempo_de_aluguel INTEGER,
                reputação TEXT NOT NULL
                )""")


class Material:
    # id = ""                                         #identificação para rastreamento
    # nome = ""                                       #nome do livro
    # tipo = ""                                       #artigo, livro ou documentário
    # autor = ""                                      #nome do autor no livro
    # status = ""                                     #disponível ou ou indisponível para aluguel
    # ano_de_publicacao = ""                          #ano de publicação do conteúdo

    def __init__(self, nome, autor, ano_de_publicacao, status):
        self.nome = nome
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.status = status


class Usuario:

    def __init__(self, login):

        self.login = login
        self.sistema = Sistema()
        self.acesso_usuario(login)

    def acesso_usuario(self, login):
        try:
            print("-" * 40)
            print("--Biblioteca virtual iniciada--")
            print(f"\nOlá {login}! Seja bem vindo!")
            print("O que deseja?")
            print("""1 - Encontrar Material
2 - Devolver Material
3 - Histórico
4 - Sair""")

            usuario = int(input("Selecione apenas o número da opção desejada: "))

            if usuario == 0:
                Administrador(login)
            elif usuario == 1:
                self.sistema.busca()
            elif usuario == 2:
                self.sistema.devolucao()
            elif usuario == 3:
                Historico(login)
            elif usuario == 4:
                print("Saindo...")

        except ValueError as error:
            print(f"Erro ocorrido: {error}")


class Administrador:

    def __init__(self, login):
        self.login = login
        self.sistema_adm = SistemaAdministrador()
        self.acesso_adm(login)

    def acesso_adm(self, login):

        senhas = {1206: "admin1", 458: "admin2", 916: "admin3"}
        senha = int(
            input(
                "Você está tentando acessar o sistema de administração. Coloque sua senha de 4 dígitos: "
            )
        )

        if senha in senhas:
            login = senhas[senha]
            print("Acesso concedido")
        else:
            print("Acesso Negado")
            return

        print("-" * 40)
        print("--Biblioteca virtual iniciada--")
        print(f"\nOlá {login}! Seja bem vindo ao ambiente de administração!")
        print("O que deseja?")
        print("""1 - Postar Material
2 - Deletar Material
3 - Encontrar Material
4 - Sair""")

        administrador = int(input("Selecione a opção desejada: "))
        if administrador == 1:
            self.sistema_adm.adicionar_material()
        elif administrador == 2:
            self.sistema_adm.deletar_material()
        elif administrador == 3:
            self.sistema_adm.busca()
        elif administrador == 4:
            print("Saindo...")


class Sistema:

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
    def __init__(self, login):
        self.login = login

        cursor.execute("SELECT FROM historico WHERE nome = ?", (login))
        print(cursor.fetchall())


pessoa1 = Usuario("Arthur")
