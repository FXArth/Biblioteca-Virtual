# Skill: Daily Context

## Objetivo
Recuperar o contexto do usuário a partir do `vault/`, gerar um briefing de retomada no início da sessão, e registrar o encerramento do dia — garantindo continuidade sem depender da memória do usuário nem da sua própria janela de contexto.

## Mecânicas Principais

### 1. Abertura de sessão ("Bom dia, RAI", "Boa tarde, RAI", "Resumo", início de conversa)

Ler silenciosamente, nesta ordem:
- `vault/perfil.md` (contexto permanente do usuário);
- a nota diária mais recente em `vault/daily/` (não necessariamente "ontem" —
  pode ser sexta-feira numa segunda de manhã);
- os arquivos em `vault/projetos/` referenciados nessa última nota.

Gerar uma resposta estruturada:
- **Saudação:** breve, amigável, sem exagero.
- **Onde paramos:** resumo do que estava sendo construído em cada trilha ativa
  mencionada na última nota (pode ser mais de uma).
- **Ponto de Atenção:** se havia uma dificuldade registrada, ofereça uma explicação,
  dica ou analogia curta para destravar — sem resolver o problema inteiro.
- **Plano de Ação:** apresente o próximo passo e o que está pendente.

Regra Socrática: não resolva os passos pendentes nem escreva o código que falta.
Apenas mostre o palco e pergunte por onde o usuário quer começar.

**Depois que o usuário escolher o que vai atacar nesta sessão:**
1. Verifique em qual branch git você está agora (`git branch --show-current`).
2. Decida se precisa de uma branch nova, usando o critério da skill
   `git-versioning` (só cria branch para tarefa com escopo real — recurso ou
   correção não-trivial; não cria para ajuste pequeno ou continuação do que
   já está em andamento).
3. Se já estiver numa branch referente à mesma tarefa escolhida (ex: você
   continuou ontem o que começou hoje), não cria branch nova — segue nela.
4. Se precisar de branch nova, delegue a criação para a skill
   `git-versioning` (segue a mesma aprovação por comando das demais ações
   git) — nunca crie a branch antes de confirmar com o usuário o nome
   proposto.

### 2. Encerramento de sessão ("Boa noite, RAI!", "Por hoje é só!", fim de conversa)

Ao detectar um encerramento explícito:
1. Resumir o que foi feito na sessão (não a conversa inteira — só o que importa para continuidade futura): decisões tomadas, o que foi concluído, onde travou. Qualquer item de código que for descrito como "concluído" (bug corrigido, função implementada) segue a mesma verificação obrigatória da seção 3 da skill `project-sync` — reabrir e conferir o arquivo real antes de escrever, nunca confiar só no que foi dito na conversa.
2. Escrever/atualizar `vault/daily/AAAA-MM-DD.md` com essa estrutura:

```markdown
# AAAA-MM-DD

## Trilhas tocadas
- [nome do projeto/tema]

## Concluído
- ...

## Decisões
- ...

## Dificuldade atual
- ...

## Próximo passo
- ...

## Pendente
- ...
```

3. Se algo indicar mudança de estado relevante de um projeto (não apenas o dia), atualizar também o arquivo correspondente em `vault/projetos/nome.md`.
4. Informar claramente ao usuário o que foi escrito e em quais arquivos, antes de encerrar (nunca escrever em silêncio — respeitar a diretriz global de transparência sobre arquivos).
5. Acionamento do Safe Protocol (Integração com code-editing): antes de salvar
   as alterações nos arquivos do `vault/`, você DEVE acionar as regras da
   skill `code-editing` — apresente o conteúdo atualizado dos arquivos `.md`
   como proposta visual (Diff). A escrita real no disco só acontece após o
   "Accept" explícito do usuário.
6. Oferecer o versionamento da sessão ("quer que eu prepare o commit de
   hoje?"). Se confirmado, a execução passa inteiramente para a skill
   `git-versioning` — comandos de terminal (`git add`, `commit`, `push`) não
   usam o Diff visual do `code-editing` (que serve para conteúdo de arquivo,
   não para comandos), e sim a aprovação individual por comando descrita em
   `git-versioning`.

### 3. Multi-trilha

Uma mesma nota diária pode conter mais de uma trilha (ex: um projeto de código e uma decisão pessoal no mesmo dia). Não force tudo em um único "assunto do dia" — reflita a sessão como ela de fato aconteceu.

## Regras de Ativação
- Respeitar as diretrizes globais de `GEMINI.md`.
- Não confundir esta skill com `decision-support`: aqui o foco é continuidade e memória, não deliberação sobre uma escolha específica.
- Ao manipular arquivos ou sugerir comandos de terminal, a skill code-editing atua como um interceptador de segurança obrigatório. Nenhuma ação de I/O (Input/Output) ocorre sem o "Accept" visual.