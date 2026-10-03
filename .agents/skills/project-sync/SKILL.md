# Skill: Project Sync (Atualização de Projeto)

## Objetivo
Permitir que o usuário, a qualquer momento e por comando explícito, peça para o
agente analisar o estado atual de um projeto (código + conversa) e atualizar o
arquivo de memória correspondente em `vault/projetos/`. Não depende do fluxo de
abertura/encerramento de sessão da skill `daily-context`.

## Mecânicas Principais

### 1. Gatilho explícito, nunca automático
Esta skill só ativa quando o usuário pedir claramente, com frases como:
"atualiza o projeto", "analisa e atualiza", "atualiza a memória disso",
"salva o que fizemos aqui". Nunca roda por conta própria, por horário, ou
"aproveitando" outro comando.

### 2. Identificação do projeto em foco
Antes de escrever qualquer coisa, identifique qual projeto está em pauta:
- Pela pasta/arquivo que está aberto ou sendo discutido na conversa atual;
- Se houver ambiguidade (ex: mais de um projeto mencionado na sessão),
  pergunte qual antes de atualizar.

Se ainda não existir `vault/projetos/<nome-do-projeto>.md` para esse projeto,
crie um novo seguindo a mesma estrutura usada nos demais (não é preciso pedir
permissão para criar o arquivo, mas informe que ele foi criado).

### 3. Verificação obrigatória antes de marcar como "Concluído"

Esta é uma trava, não uma recomendação: **nenhum item pode ser escrito como
"Concluído" em `vault/projetos/<nome>.md` sem verificação direta na fonte**.
A sua própria fala anterior na conversa — inclusive uma frase sua dizendo "já
corrigi isso" — não é evidência suficiente. Já aconteceu de um bug ser
reportado como resolvido em `vault/` enquanto o código real continuava
quebrado; essa checagem existe para que isso não se repita.

Antes de escrever qualquer item em "Concluído" que se refira a uma mudança de
código (correção de bug, nova função, refatoração):
1. Reabra o arquivo de código real envolvido (não confie na memória da
   conversa, releia o arquivo agora);
2. Confirme, linha por linha se necessário, que o trecho citado como
   corrigido de fato está diferente do estado anterior e resolve o que foi
   descrito;
3. Se não for possível verificar (arquivo não encontrado, mudança não
   aplicada, ou você não tem certeza), **não escreva como "Concluído"** —
   registre em "Pendente" com uma nota tipo "alteração relatada na conversa,
   mas não confirmada no código" e avise o usuário explicitamente dessa
   divergência antes de prosseguir.

Para itens não-técnicos (decisões, preferências), a verificação é mais simples
— confirme contra o que foi de fato dito na conversa, não contra um resumo
anterior que você mesmo gerou.

### 4. Atualização incremental, não substituição total
Ao atualizar `vault/projetos/<nome>.md`:
- Preserve o que já estava correto em "Concluído" — apenas adicione o que
  mudou, não reescreva do zero;
- Mova para "Concluído" o que foi resolvido desde a última atualização;
- Atualize "Pendente" e "Dificuldade atual" com o que ficou em aberto;
- Atualize "Próximo passo" com base no que faz mais sentido atacar a seguir.

### 5. Transparência obrigatória
Depois de escrever, informe ao usuário exatamente o que mudou no arquivo antes
de seguir em frente — nunca atualizar em silêncio (regra global do
`GEMINI.md`).

## Regras de Ativação
- Só ativa mediante comando explícito do usuário — nunca em segundo plano,
  por gatilho de tempo, ou como efeito colateral de outro pedido.
- Não substitui a `daily-context`: aquela cuida do briefing de "bom
  dia"/"boa noite"; esta cuida do estado de um projeto específico, chamável a
  qualquer momento, independente da hora do dia.
- A verificação obrigatória da seção 3 não é opcional nem pode ser pulada por
  o usuário estar com pressa ou já ter afirmado que o bug foi corrigido — ela
  existe justamente para o caso em que essa afirmação está errada.