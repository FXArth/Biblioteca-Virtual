# Projeto: Sistema Bibliotecário (Python / POO)

## O que é
Projeto de estudo para entender Programação Orientada a Objetos em Python,
usando um sistema bibliotecário como exemplo prático.

## Conceito atual
Classes, atributos e o método construtor `__init__`; como `self` funciona na
prática para acessar atributos da instância.

## Concluído
- Bug na inicialização da classe `Material` resolvido (parâmetros alinhados: `nome`, `tipo`, `autor`, `ano`, `edicao`, `status`).
- Bug de sintaxe SQL na classe `Historico` corrigido (tupla e `SELECT *`).
- Refatoração de POO: Desacoplamento dos menus interativos dos construtores `__init__` das classes `Usuario` e `Administrador`.
- Criação das tabelas de banco de dados (`leitores` e `administradores`) no SQLite.
- TelaInicial (Reception) criada, aplicando SRP (Responsabilidade Única).
- Lógica de Cadastro (INSERT) de Leitores implementada com Queries Seguras.
- Sistema de Login de Leitores (SELECT) implementado e integrado ao menu do sistema.

## Próximo passo
- Estruturar a lógica de Cadastro/Login para a tabela de Administradores, espelhando a segurança feita para os Leitores.

## Pendente
- Lógica de cadastro (INSERT) para administradores.
- Remover o "em construção" e integrar o painel real da classe `SistemaAdministrador` para usuários logados como admin.

## Dificuldade atual
- Nenhuma no momento.