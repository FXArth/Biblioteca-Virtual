# Projeto: Sistema Bibliotecário (Python / POO)

## O que é
Projeto de estudo para entender Programação Orientada a Objetos em Python,
usando um sistema bibliotecário como exemplo prático.

## Conceito atual
Compreensão sólida de Classes vs Objetos, passagem de parâmetros no `__init__`, escopo e leitura de atributos via `self`, e a diferença entre Herança (É um) e Composição (Tem um).

## Concluído
- Criação das tabelas de banco de dados (`leitores` e `administradores`) no SQLite.
- TelaInicial (Reception) criada, aplicando SRP (Responsabilidade Única).
- Sistema de Login e Cadastro (INSERT/SELECT) de Leitores implementado com Queries Seguras.
- Refatoração de POO: A classe `Usuario` agora recebe seus dados (`id`, `nome`, `cpf`, `email`) diretamente do banco via construtor, sem armazenar a senha.
- Refatoração de POO: A classe `Historico` foi reestruturada para usar Composição em vez de Herança, recebendo o nome do dono em seu construtor e realizando buscas independentes.
- Unificação de código: Plano de Estudos de POO totalmente concluído e as melhorias aplicadas foram unificadas (merge) na branch principal (`main`).

## Próximo passo
- Estruturar a lógica de Cadastro/Login para a tabela de Administradores na `TelaInicial`.

## Pendente
- Lógica de cadastro (INSERT) para administradores.
- Remover o "em construção" da opção 0 e integrar o painel real da classe `SistemaAdministrador` para administradores logados.

## Dificuldade atual
- Nenhuma. Base teórica de Orientação a Objetos foi estabilizada com sucesso.