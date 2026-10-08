# Projeto: Sistema Bibliotecário (Python / POO)

## O que é
Projeto de estudo para entender Programação Orientada a Objetos em Python,
usando um sistema bibliotecário como exemplo prático.

## Conceito atual
Compreensão sólida de Classes vs Objetos, escopo e composição.
Navegação entre menus, Call Stack (Pilha de chamadas) e loops infinitos (`while True`).

## Concluído
- Criação das tabelas de banco de dados (`leitores` e `administradores`) no SQLite.
- TelaInicial (Reception) criada, aplicando SRP (Responsabilidade Única).
- Sistema de Login e Cadastro (INSERT/SELECT) de Leitores implementado com Queries Seguras.
- Refatoração de POO: A classe `Usuario` agora recebe seus dados (`id`, `nome`, `cpf`, `email`) diretamente do banco via construtor, sem armazenar a senha.
- Refatoração de POO: A classe `Historico` foi reestruturada para usar Composição em vez de Herança, recebendo o nome do dono em seu construtor e realizando buscas independentes.
- Unificação de código: Plano de Estudos de POO totalmente concluído e as melhorias aplicadas foram unificadas (merge) na branch principal (`main`).
- Fluxo de Administradores: Adicionados submenus na `TelaInicial` redirecionando o fluxo de login/cadastro entre leitores e administradores, instanciando `Administrador` e acessando `SistemaAdministrador()`.

## Próximo passo
- Envolver todos os menus em laços principais (`while True`) e aplicar tratamento de erros para que o sistema se torne contínuo.

## Pendente
- Laços infinitos na TelaInicial e nos Submenus.
- Opções lógicas de retorno (`break`) para navegar adequadamente entre os blocos sem encerrar abruptamente.

## Dificuldade atual
- Nenhuma. Código segue muito bem arquitetado e pronto para a próxima evolução de interface.