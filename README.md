# Trabalho Flood Fill

## Descrição do projeto

Este projeto implementa o **Algoritmo Flood Fill** (Preenchimento por Inundação) para simular o mapeamento inteligente de um terreno por um sistema de robôs autônomos.

O objetivo é identificar e preencher automaticamente todas as regiões livres e conectadas em um grid 2D, separando-as com cores distintas. Os obstáculos (barreiras) funcionam como limites que impedem a expansão do preenchimento, garantindo que as regiões desconectadas sejam isoladas e mapeadas individualmente.

## Introdução sobre o problema Flood Fill

O problema abordado consiste em interpretar um grid bidimensional n x m, onde células com valor (0) representam terreno navegável e células com valor (1) representam obstáculos.

O desafio principal é que o terreno pode conter múltiplas áreas navegáveis isoladas umas das outras por paredes de obstáculos. O robô precisa não apenas mapear uma área, mas também identificar todas as regiões livres desconectadas do mapa, atribuindo um identificador único (uma "cor" numérica: 2, 3, 4...) para cada região distinta. Além disso, ele deve evitar os obstáculos no terreno e não ultrapassá-los, mantendo-os com o valor (1).

## Instruções para executar o projeto

### Pré-requisitos

Ter Python 3 instalado.

### Execução

1. Clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

- Windows:
  
```bash
python main.py
```

* macOS / Linux:

```bash
python3 main.py
```

O programa exibirá o **grid inicial** e o **grid final preenchido** no terminal.

### Execução com interface gráfica (GUI animada)

Para visualizar o processo de preenchimento **com animação passo a passo**, execute:

```bash
python main.py --gui
```

A interface gráfica abrirá mostrando o grid inicial e irá colorir as células automaticamente ao longo do tempo.

### Execução com grid aleatório (ponto extra)

Você pode pedir para o programa gerar automaticamente um grid aleatório.

Sintaxe:

```bash
python main.py --random N M --p PROB
```

Onde:

* `N M` = dimensões do grid
* `--p` = probabilidade de obstáculos (0.0 a 1.0)

Exemplo (10×15 com 35% de obstáculos):

```bash
python main.py --random 10 15 --p 0.35
```

#### Seed

Para repetir o mesmo grid (reprodutível):

```bash
python main.py --random 10 15 --p 0.35 --seed 42
```

#### Aleatório com interface gráfica

```bash
python main.py --random 20 20 --p 0.3 --gui
```

#### Células pré-coloridas (opcional)

Para gerar poucas células já coloridas (>1):

```bash
python main.py --random 12 12 --p 0.25 --prefilled
```

### Coordenada inicial no modo aleatório (manual ou automática)

No modo aleatório, você pode escolher como definir a célula inicial:

#### Start automático (padrão)

O programa escolhe sozinho uma célula navegável `(0)`:

```bash
python main.py --random 10 10 --p 0.3 --start auto
```

#### Start manual

Você define a coordenada inicial:

```bash
python main.py --random 10 10 --p 0.3 --start manual --x 2 --y 3
```

> Se a coordenada manual cair em obstáculo ou fora do grid, o programa avisa e troca automaticamente para um start válido.

---

## Funcionamento do Algoritmo Flood Fill

1. Verifica se a célula inicial `(x,y)` é válida e navegável.
2. Preenche toda a região conectada de `0` com a cor atual (começando em 2).
3. Procura no grid a próxima célula `0`.
4. Incrementa a cor e repete o preenchimento.
5. Finaliza quando todas as áreas navegáveis estiverem preenchidas.

---

## Exemplos de Entrada e Saída

Os exemplos abaixo ilustram o funcionamento do Flood Fill em diferentes situações, conforme solicitado no enunciado: grids manuais e grids aleatórios gerados automaticamente.

### Exemplo 1 — Manual

#### Comando

```bash
python main.py
```

#### Entrada

```
4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
```

#### Saída

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

---

### Exemplo 2 — Manual

#### Comando

```bash
python main.py
```

#### Entrada

```
4 5
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
0 2
```

#### Saída

```
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```

---

### Exemplo 3 — Aleatório 6×8 (p=0.30, seed=7)

#### Comando

```bash
python main.py --random 6 8 --p 0.30 --seed 7
```

**Grid inicial gerado**

```
0 1 0 1 0 0 1 0
1 0 1 1 0 0 1 1
0 0 0 0 0 1 0 1
1 1 0 0 1 0 0 0
0 1 1 1 0 0 0 0
0 1 0 0 1 0 0 0
```

**Grid final preenchido**

```
3 1 4 1 2 2 1 5
1 2 1 1 2 2 1 1
2 2 2 2 2 1 6 1
1 1 2 2 1 6 6 6
7 1 1 1 6 6 6 6
7 1 8 8 1 6 6 6
```

---

### Exemplo 4 — Aleatório 5×7 (p=0.40, seed=21)

#### Comando

```bash
python main.py --random 5 7 --p 0.40 --seed 21
```

**Grid inicial gerado**

```
1 0 0 0 1 0 0
0 0 1 1 1 0 1
0 1 1 1 0 0 0
0 1 1 0 1 0 1
1 0 1 0 0 0 1
```

**Grid final preenchido**

```
1 3 3 3 1 2 2
3 3 1 1 1 2 1
3 1 1 1 2 2 2
3 1 1 2 1 2 1
1 4 1 2 2 2 1
```

---

### Exemplo 5 — Aleatório 8×8 (p=0.25, seed=99)

#### Comando

```bash
python main.py --random 8 8 --p 0.25 --seed 99
```

**Grid inicial gerado**

```
0 1 1 1 0 0 0 0
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 1 0 1
0 0 0 0 0 1 1 0
0 1 0 1 0 1 0 0
1 0 1 1 0 0 0 0
```

**Grid final preenchido**

```
2 1 1 1 2 2 2 2
2 2 2 2 2 1 2 2
2 2 1 2 2 2 2 2
2 2 2 2 1 1 2 2
2 2 2 2 2 1 2 1
2 2 2 2 2 1 1 2
2 1 2 1 2 1 2 2
1 3 1 1 2 2 2 2
```

---

## Estrutura do repositório

```
.
├── main.py
├── flood_fill.py
├── gui.py
└── README.md
```