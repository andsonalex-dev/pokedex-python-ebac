# Pokedex CLI

Uma aplicação em Python de linha de comando para cadastrar e gerenciar Pokémon em uma Pokédex simples.

## Funcionalidades

- Adicionar Pokémon com nome, tipo e nível.
- Listar todos os Pokémon cadastrados em ordem alfabética.
- Remover Pokémon da Pokédex.
- Atualizar o nível de um Pokémon.
- Registrar capturas e manter o histórico.
- Exibir o histórico de capturas.

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. No terminal, acesse a pasta do projeto.
3. Execute o programa:

```bash
python main.py
```

## Menu da aplicação

Ao iniciar, o programa mostra as opções:

1. Adicionar Pokémon
2. Listar Pokémon
3. Remover Pokémon
4. Atualizar nível do Pokémon
5. Registrar captura
6. Exibir histórico de capturas
7. Sair

## Regras de validação

- O nome do Pokémon não pode ser cadastrado duas vezes.
- O tipo do Pokémon deve ser um dos já existentes na lista.
- O nível deve estar entre 1 e 100.
- A quantidade de capturas deve ser maior que 0.
- Operações de remoção, atualização e captura exigem que o Pokémon já esteja cadastrado.

## Estrutura interna

O projeto usa duas estruturas em memória:

- `pokedex`: armazena os Pokémon cadastrados com tipo, nível e total de capturas.
- `capture_history`: guarda o histórico das capturas registradas durante a execução.

## Observações

- Os dados não são salvos em arquivo; tudo é perdido ao encerrar o programa.
- O projeto não possui dependências externas.
