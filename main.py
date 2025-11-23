import argparse
import random
from copy import deepcopy
from flood_fill import color_all_regions, print_grid, is_valid
from gui import show_gui_animated

def read_input_from_stdin():
    """
    Entrada esperada:
    n m
    linha1 (m valores)
    ...
    linhan (m valores)
    x y
    """
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    x, y = map(int, input().split())
    return grid, x, y

def generate_random_grid(n, m, p_obstacle=0.3, allow_prefilled=False):
    grid = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(1 if random.random() < p_obstacle else 0)
        grid.append(row)

    if allow_prefilled:
        for _ in range(max(1, (n*m)//30)):
            i = random.randrange(n)
            j = random.randrange(m)
            if grid[i][j] == 0:
                grid[i][j] = random.choice([2, 3, 4])

    return grid

def pick_random_start(grid):
    zeros = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    return random.choice(zeros) if zeros else (0, 0)

def main():
    parser = argparse.ArgumentParser(description="Flood Fill - colorindo regiões")
    parser.add_argument("--gui", action="store_true", help="Abre interface gráfica Tkinter (com animação)")
    parser.add_argument("--no-color", action="store_true", help="Desativa cores ANSI no terminal")

    # modo aleatório
    parser.add_argument("--random", nargs=2, type=int, metavar=("N", "M"),
                        help="Gera grid aleatório N x M automaticamente")
    parser.add_argument("--p", type=float, default=0.3,
                        help="Probabilidade de obstáculo no grid aleatório (0.0 a 1.0). Padrão=0.3")
    parser.add_argument("--seed", type=int, default=None,
                        help="Seed para reprodutibilidade do grid aleatório")
    parser.add_argument("--prefilled", action="store_true",
                        help="(Opcional) Permite algumas células já coloridas no grid aleatório")

    # NOVO: escolha de start no aleatório
    parser.add_argument("--start", choices=["auto", "manual"], default="auto",
                        help="No modo aleatório, start pode ser auto (padrão) ou manual.")
    parser.add_argument("--x", type=int, help="Coordenada x inicial (uso com --start manual)")
    parser.add_argument("--y", type=int, help="Coordenada y inicial (uso com --start manual)")

    args = parser.parse_args()

    if args.random:
        n, m = args.random
        if args.seed is not None:
            random.seed(args.seed)

        grid = generate_random_grid(n, m, p_obstacle=args.p, allow_prefilled=args.prefilled)

        if args.start == "manual" and args.x is not None and args.y is not None:
            x, y = args.x, args.y
            if not is_valid(grid, x, y) or grid[x][y] != 0:
                print(f"\nCoordenada manual ({x},{y}) inválida ou não navegável. Usando start automático.")
                x, y = pick_random_start(grid)
        else:
            x, y = pick_random_start(grid)

        print(f"\nGRID ALEATÓRIO GERADO ({n}x{m}) | p_obstáculo={args.p}")
        print(f"Coordenada inicial usada: ({x}, {y})")

    else:
        grid, x, y = read_input_from_stdin()

    initial_grid = deepcopy(grid)

    print("\nGRID INICIAL:")
    print_grid(grid, colored=not args.no_color)

    final_grid = color_all_regions(grid, x, y)

    print("\nGRID FINAL PREENCHIDO:")
    print_grid(final_grid, colored=not args.no_color)

    if args.gui:
        show_gui_animated(initial_grid, x, y)

if __name__ == "__main__":
    main()
