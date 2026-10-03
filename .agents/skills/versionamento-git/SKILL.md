# Skill: Versionamento (Git)

## Objetivo
Preparar e executar o versionamento (`git add`, `git commit`, `git push`) do
que foi feito na sessão, usando a ferramenta de terminal nativa do agente —
nunca um script customizado — e sempre com aprovação explícita e individual
de cada comando antes de rodar.

## Mecânicas Principais

### 0. Branches: quando criar e quando mesclar

**Criação** (disparada pela `daily-context` no início da sessão, ao escolher a
tarefa): crie uma branch nova somente quando a tarefa tiver escopo real — um
recurso ou correção não-trivial (ex: implementar um método inteiro, corrigir
um bug que exige mudar lógica). Não crie branch para ajuste pequeno, comentário,
ou continuação de algo já em andamento na branch atual. Nomeie
semanticamente: `feat/`, `fix/`, `chore/`, `refactor/` + descrição curta (ex:
`fix/bug-historico`). Proponha o nome, espere aprovação, e só então rode
`git checkout -b <nome>` — mesma aprovação individual por comando das outras
ações desta skill.

**Merge** (não acontece no encerramento de sessão — só quando a tarefa é
dada como concluída e verificada): antes de propor o merge, confirme que a
trava de verificação da seção 3 da `project-sync` foi cumprida para tudo que
está sendo mesclado. Proponha o comando (`git checkout main` + `git merge
<branch>`), espere aprovação por comando, e só depois pergunte se a branch
antiga deve ser apagada (`git branch -d`).

### 1. Gatilho
Ativa quando o usuário pedir explicitamente ("versiona isso", "commit e
push", "sobe pro Git") ou quando a `daily-context` oferecer o versionamento
no encerramento da sessão e o usuário confirmar que quer prosseguir. Nunca
dispara sozinha, e nunca assume que "fim de sessão" significa "pode
commitar".

### 2. Mensagem de commit sujeita à verificação
Antes de escrever a mensagem de commit, aplique a mesma trava de verificação
da seção 3 da skill `project-sync`: nenhuma palavra como "corrige", "resolve"
ou "implementa" pode entrar na mensagem referindo-se a algo que não foi
confirmado no código real nesta sessão. Se uma mudança foi tentada mas não
verificada, ou foi feita por você mas não revisada pelo usuário via Accept,
ela não entra como concluída na mensagem — ou fica de fora, ou a mensagem
reflete o estado real ("tentativa de correção, pendente de verificação").

Use o padrão Conventional Commits (`feat`, `fix`, `docs`, `chore`,
`refactor`) para o título, com corpo explicando o que mudou e por quê quando
não for óbvio.

### 3. Execução: um comando por vez, uma aprovação por vez
- Apresente o comando exato antes de rodar (ex: mostre o texto completo de
  `git commit -m "..."` antes de executar).
- Rode usando a ferramenta de terminal integrada do agente, não um script
  Python ou qualquer camada intermediária.
- Espere a aprovação individual de cada comando. Nunca ofereça ou aceite
  "aprovar tudo de uma vez" para a sequência de versionamento.
- A ordem é sempre `git add` → `git commit` → `git push`, cada um com sua
  própria aprovação, mesmo que o usuário já tenha aprovado os anteriores na
  mesma sessão.

### 4. Push é sempre o passo mais isolado
Mesmo que `add` e `commit` já tenham sido aprovados, peça confirmação
separada antes do `push` — é o ponto em que a mudança sai da sua máquina e
vai para o repositório remoto, mais difícil de desfazer depois.

### 5. Falhas são reportadas como realmente aconteceram
Se um comando falhar (conflito, rejeição do remoto, erro de autenticação),
mostre a saída real do terminal. Nunca diga que um comando funcionou sem ter
visto o retorno dele confirmando isso.

## Regras de Ativação
- Sempre respeitar as diretrizes globais do `GEMINI.md`.
- Nunca executar `git add`, `git commit` ou `git push` sem aprovação
  individual do usuário para aquele comando específico.
- A mensagem de commit segue a mesma verificação obrigatória da skill
  `project-sync` (seção 3) — não descrever como resolvido o que não foi
  confirmado no código.
- Esta skill cuida do versionamento depois que uma alteração de código já foi
  revisada e aceita; ela não substitui o checkpoint visual da `code-editing`
  para a alteração em si.