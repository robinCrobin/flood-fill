import argparse
import random
import sys
from copy import deepcopy
from flood_fill import color_all_regions, print_grid, is_valid
from gui import show_gui_animated

def read_input_interactive():
    """
    Lê entrada interativa do usuário com validação.
    """
    print("\n" + "=" * 60)
    print("FLOOD FILL - ALGORITMO DE PREENCHIMENTO DE REGIÕES")
    print("=" * 60)
    
    print("\nDigite as dimensões do grid (N M):")
    N, M = map(int, input().split())
    
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
            return None, None, None
        
        grid.append(linha)
    
    print(f"\nDigite as coordenadas iniciais (x y):")
    print(f"Onde x está entre 0 e {N-1}, e y está entre 0 e {M-1}")
    x, y = map(int, input().split())
    
    if not is_valid(grid, x, y):
        print(f"ERRO: Coordenadas ({x}, {y}) estão fora dos limites do grid!")
        return None, None, None
    
    if grid[x][y] != 0:
        print(f"ERRO: A célula inicial ({x}, {y}) não é navegável (valor = {grid[x][y]})!")
        print("A célula inicial deve ter valor 0 (terreno navegável).")
        return None, None, None
    
    return grid, x, y

def read_input_from_stdin():
    """
    Entrada esperada do stdin (para redirecionamento):
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
    parser = argparse.ArgumentParser(
        description="Flood Fill - Algoritmo de preenchimento de regiões",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
        Exemplos de uso:
        # Modo interativo (padrão)
        python3 main.py
        
        # Grid aleatório com GUI
        python3 main.py --random 10 10 --gui
        
        # Grid aleatório sem cores no terminal
        python3 main.py --random 8 8 --no-color
        
        # Entrada via arquivo
        python3 main.py < entrada.txt
        
        # Entrada via pipe com GUI
        echo "3 3\\n0 1 0\\n1 0 1\\n0 1 0\\n1 1" | python3 main.py --gui
                '''
    )
    
    parser.add_argument("--gui", action="store_true", 
                        help="Abre interface gráfica Tkinter com animação")
    parser.add_argument("--no-color", action="store_true", 
                        help="Desativa cores ANSI no terminal")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Força modo interativo com mensagens detalhadas")

    # Modo aleatório
    parser.add_argument("--random", nargs=2, type=int, metavar=("N", "M"),
                        help="Gera grid aleatório N x M automaticamente")
    parser.add_argument("--p", type=float, default=0.3,
                        help="Probabilidade de obstáculo no grid aleatório (0.0 a 1.0). Padrão=0.3")
    parser.add_argument("--seed", type=int, default=None,
                        help="Seed para reprodutibilidade do grid aleatório")
    parser.add_argument("--prefilled", action="store_true",
                        help="Permite algumas células já coloridas no grid aleatório")

    # Escolha de coordenada inicial
    parser.add_argument("--start", choices=["auto", "manual"], default="auto",
                        help="No modo aleatório, start pode ser auto (padrão) ou manual")
    parser.add_argument("--x", type=int, help="Coordenada x inicial (uso com --start manual)")
    parser.add_argument("--y", type=int, help="Coordenada y inicial (uso com --start manual)")

    args = parser.parse_args()

    # Determinar modo de entrada
    if args.random:
        # Modo aleatório
        n, m = args.random
        if args.seed is not None:
            random.seed(args.seed)

        grid = generate_random_grid(n, m, p_obstacle=args.p, allow_prefilled=args.prefilled)

        if args.start == "manual" and args.x is not None and args.y is not None:
            x, y = args.x, args.y
            if not is_valid(grid, x, y) or grid[x][y] != 0:
                print(f"\n⚠️  Coordenada manual ({x},{y}) inválida ou não navegável.")
                print("   Usando coordenada automática...")
                x, y = pick_random_start(grid)
        else:
            x, y = pick_random_start(grid)

        print(f"\n🎲 GRID ALEATÓRIO GERADO ({n}x{m})")
        print(f"   Probabilidade de obstáculo: {args.p}")
        print(f"   Coordenada inicial: ({x}, {y})")
        
    else:
        # Modo padrão: interativo ou stdin
        if sys.stdin.isatty():
            # Terminal interativo
            grid, x, y = read_input_interactive()
            if grid is None:
                return
        else:
            # Stdin redirecionado (pipe ou arquivo)
            grid, x, y = read_input_from_stdin()

    # Salvar grid original para animação
    initial_grid = deepcopy(grid)

    # Exibir grid original
    print("\n" + "=" * 60)
    print("GRID ORIGINAL:")
    print("=" * 60)
    print_grid(grid)

    # Processar flood fill
    print("\n" + "=" * 60)
    print("PROCESSAMENTO DO FLOOD FILL:")
    print("=" * 60)
    final_grid = color_all_regions(grid, x, y)

    # Exibir grid final
    print("\n" + "=" * 60)
    print("GRID APÓS PREENCHIMENTO:")
    print("=" * 60)
    print_grid(final_grid)

    # Animação GUI
    if args.gui:
        # GUI automática (sem perguntar)
        print("\n✨ Abrindo janela de animação...")
        try:
            show_gui_animated(initial_grid, x, y, cell_size=50, delay_ms=50)
        except Exception as e:
            print(f"❌ Erro ao abrir GUI: {e}")
    else:
        # Perguntar se deseja ver animação
        if sys.stdin.isatty():  # Só pergunta se terminal é interativo
            print("\n" + "=" * 60)
            print("🎬 Deseja ver a animação do preenchimento? (s/n): ", end="")
            resposta = input().strip().lower()
            
            if resposta in ['s', 'sim', 'y', 'yes']:
                try:
                    print("\n✨ Abrindo janela de animação...")
                    print("💡 Dica: A animação mostra o preenchimento passo a passo!")
                    show_gui_animated(initial_grid, x, y, cell_size=50, delay_ms=50)
                except ImportError:
                    print("\n❌ ERRO: Módulo 'gui.py' não encontrado!")
                    print("   Certifique-se de que o arquivo 'gui.py' está no mesmo diretório.")
                except Exception as e:
                    print(f"\n❌ ERRO ao abrir animação: {e}")
            else:
                print("\n✅ Programa finalizado!")

if __name__ == "__main__":
    main()
