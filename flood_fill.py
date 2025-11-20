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