import sys
sys.setrecursionlimit(2000) 

def is_valid(grid, x, y):
    """
    Verifica se a célula (x, y) está dentro dos limites do grid.
    """
    N = len(grid)
    M = len(grid[0])
    return 0 <= x < N and 0 <= y < M

def flood_fill_recursive(grid, x, y, new_color):
    """
    Implementa o algoritmo Flood Fill recursivamente, 
    preenchendo uma única região navegável (valor 0).
    """
    if not is_valid(grid, x, y):
        return
    
    if grid[x][y] != 0:
        return
    
    grid[x][y] = new_color
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        flood_fill_recursive(grid, new_x, new_y, new_color)


def color_all_regions(grid, start_x, start_y):
    """
    Função que gerencia as cores e analisa o terreno.
    """
    current_color = 2 
    
    print(f"Iniciando pintura na coordenada ({start_x}, {start_y}) com a cor {current_color}...")

    if is_valid(grid, start_x, start_y) and grid[start_x][start_y] == 0:
        flood_fill_recursive(grid, start_x, start_y, current_color)
        current_color += 1 
    else:
        print("A coordenada inicial não é válida ou é um obstáculo.")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0: 
                flood_fill_recursive(grid, i, j, current_color)
                current_color += 1 
    
    return grid