import sys
from collections import deque

sys.setrecursionlimit(10**6)

def is_valid(grid, x, y):
    """Verifica se (x,y) está dentro do grid."""
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def flood_fill_iterative(grid, x, y, new_color):
    """
    Flood Fill iterativo (BFS).
    Preenche apenas células com valor 0.
    """
    if not is_valid(grid, x, y) or grid[x][y] != 0:
        return

    q = deque()
    q.append((x, y))
    grid[x][y] = new_color

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(grid, nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = new_color
                q.append((nx, ny))

def find_next_zero(grid):
    """Retorna a próxima célula (i,j) com valor 0, ou None se não houver."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def color_all_regions(grid, start_x, start_y, first_color=2):
    """
    Pinta todas as regiões 0 desconectadas:
    - Começa pela coordenada inicial se for navegável (0).
    - Caso contrário, procura a primeira célula 0 no grid.
    - Usa cores: 2,3,4,... (incrementando por região).
    - Mantém obstáculos (1) e regiões já coloridas (>1).
    """
    if not grid or not grid[0]:
        return grid

    color = first_color

    if is_valid(grid, start_x, start_y) and grid[start_x][start_y] == 0:
        flood_fill_iterative(grid, start_x, start_y, color)
        color += 1

    while True:
        nxt = find_next_zero(grid)
        if nxt is None:
            break
        x, y = nxt
        flood_fill_iterative(grid, x, y, color)
        color += 1

    return grid

def flood_fill_steps(grid, x, y, new_color):
    """
    Flood Fill iterativo que emite passos:
    yield (cx, cy, new_color) a cada célula colorida.
    """
    if not is_valid(grid, x, y) or grid[x][y] != 0:
        return

    q = deque()
    q.append((x, y))
    grid[x][y] = new_color
    yield (x, y, new_color)

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(grid, nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = new_color
                yield (nx, ny, new_color)
                q.append((nx, ny))

def color_all_regions_steps(grid, start_x, start_y, first_color=2):
    """
    Versão do color_all_regions que gera passos:
    yield (x, y, color) conforme colore cada célula.
    """
    if not grid or not grid[0]:
        return

    color = first_color

    if is_valid(grid, start_x, start_y) and grid[start_x][start_y] == 0:
        for step in flood_fill_steps(grid, start_x, start_y, color):
            yield step
        color += 1

    while True:
        nxt = find_next_zero(grid)
        if nxt is None:
            break
        x, y = nxt
        for step in flood_fill_steps(grid, x, y, color):
            yield step
        color += 1

ANSI_COLORS = {
    0: "\033[97m",   # branco
    1: "\033[90m",   # cinza (obstáculo)
    2: "\033[91m",   # vermelho
    3: "\033[93m",   # amarelo/laranja
    4: "\033[92m",   # verde
    5: "\033[94m",   # azul
    6: "\033[95m",   # magenta
    7: "\033[96m",   # ciano
}
ANSI_RESET = "\033[0m"

def print_grid(grid):
    """
    Exibe o grid no terminal com formatação visual completa:
    - Índices de linhas e colunas
    - Cores ANSI para melhor visualização
    - Símbolos especiais para terrenos e obstáculos
    """
    if not grid:
        print("Grid vazio!")
        return
    
    N = len(grid)
    M = len(grid[0]) if grid else 0
    
    print("\n    ", end="")
    for j in range(M):
        print(f"{j:3}", end=" ")
    print()
    print("   " + "-" * (M * 4 + 1))
    
    for i in range(N):
        print(f"{i:2} |", end=" ")
        for j in range(M):
            valor = grid[i][j]
            cor = ANSI_COLORS.get(valor, "\033[37m")
            
            # Usa símbolos especiais para valores 0 e 1, números para cores
            if valor == 0:
                simbolo = "  ."  # Terreno navegável
            elif valor == 1:
                simbolo = "  #"  # Obstáculo
            else:
                simbolo = f"{valor:3}"  # Cores preenchidas (2, 3, 4, ...)
            
            # Aplica cor ANSI ao símbolo/número
            print(f"{cor}{simbolo}{ANSI_RESET}", end=" ")
        print()
    print()

# Este módulo contém as funções principais do algoritmo Flood Fill.
# Para executar o programa, use: python3 main.py