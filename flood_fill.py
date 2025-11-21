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


def main():
    # Entrada 1: Dimensões do grid N x M
    print("\nDigite as dimensões do grid (N M):")
    N, M = map(int, input().split())
    
    # Entrada 2: O grid em si
    print(f"\nDigite o grid {N}x{M}:")
    print("  0 = Terreno navegável (branco)")
    print("  1 = Obstáculo (preto)")
    print("  2, 3, 4... = Cores já preenchidas")
    print("\nInsira cada linha com valores separados por espaço:")
    
    grid = []
    for i in range(N):
        print(f"Linha {i + 1}: ", end="")
        linha = list(map(int, input().split()))
        
        if len(linha) != M:
            print(f"ERRO: A linha deve ter {M} valores!")
            return
        
        grid.append(linha)
    
    print(f"\nDigite as coordenadas iniciais (x y):")
    print(f"Onde x está entre 0 e {N-1}, e y está entre 0 e {M-1}")
    x, y = map(int, input().split())
    
    if not is_valid(grid, x, y):
        print(f"ERRO: Coordenadas ({x}, {y}) estão fora dos limites do grid!")
        return
    
    if grid[x][y] != 0:
        print(f"ERRO: A célula inicial ({x}, {y}) não é navegável (valor = {grid[x][y]})!")
        print("A célula inicial deve ter valor 0 (terreno navegável).")
        return
    
    print("\nGRID ORIGINAL:")
    print_grid(grid)
    
    print("\nPROCESSAMENTO DO FLOOD FILL:")
    color_all_regions(grid, x, y)
    
    print("\nGRID APÓS PREENCHIMENTO:")
    print_grid(grid)

def print_grid(grid):
    """
    Exibe o grid de forma formatada e visual.
    """
    if not grid:
        print("Grid vazio!")
        return
    
    N = len(grid)
    M = len(grid[0])
    
    print("\n    ", end="")
    for j in range(M):
        print(f"{j:3}", end=" ")
    print()
    print("   " + "-" * (M * 4 + 1))
    
    for i in range(N):
        print(f"{i:2} |", end=" ")
        for j in range(M):
            valor = grid[i][j]
            if valor == 0:
                print(f"  .", end=" ") 
            elif valor == 1:
                print(f"  #", end=" ")  
            else:
                print(f"{valor:3}", end=" ")  
        print()
    print()

if __name__ == "__main__":
    main()