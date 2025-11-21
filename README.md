# Trabalho Flood Fill
## Descrição do projeto
Este projeto implementa o **Algoritmo Flood Fill** (Preenchimento por Inundação) para simular o mapeamento inteligente de um terreno por um sistema de robôs autônomos.

O objetivo é identificar e preencher automaticamente todas as regiões livres e conectadas em um grid 2D, separando-as com cores distintas. Os obstáculos (barreiras) funcionam como limites que impedem a expansão do preenchimento, garantindo que as regiões desconectadas sejam isoladas e mapeadas individualmente.

## Introdução sobre o problema Flood Fill
O problema abordado consiste em interpretar um grid bidimensional n x m, onde células com valor (0) representam terreno navegável e células com valor (1) representam obstáculos.

O desafio principal é que o terreno pode conter múltiplas áreas navegáveis isoladas umas das outras por paredes de obstáculos. O robô precisa não apenas mapear uma área, mas também identificar todas as regiões livres desconectadas do mapa, atribuindo um identificador único (uma "cor" numérica: 2, 3, 4...) para cada região distinta. Além disso, ele deve evitar os obstáculos no terreno e não ultrapassá-los, mantendo-os com o valor (1).

## Instruções para executar o projeto
### Pré-requisitos:
Ter o Python instalado.

### Execução:
1. Clone este repositório.

2. Abra seu terminal e navegue até a pasta do projeto.

3. Execute o arquivo main.py:

    • No Windows execute:
    
    ```python main.py```
    
    • No macOS ou Linux execute:
    
    ```python3 main.py```

O programa exibirá o grid original, o processo de coloração por região e o grid final mapeado.

## Funcionamento do Algoritmo Flood Fill


## Exemplos de Entrada e Saída
