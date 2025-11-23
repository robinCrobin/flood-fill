import tkinter as tk
from copy import deepcopy
from flood_fill import color_all_regions_steps

PALETTE = {
    0: "#FFFFFF",  # branco (navegável)
    1: "#000000",  # preto (obstáculo)
    2: "#FF4C4C",  # vermelho
    3: "#FFA94C",  # laranja
    4: "#FFE14C",  # amarelo
    5: "#7DFF4C",  # verde claro
    6: "#4CC3FF",  # azul claro
    7: "#B84CFF",  # roxo
}

def show_gui_animated(initial_grid, start_x, start_y, cell_size=40, delay_ms=35):
    """
    Mostra e anima o preenchimento:
    - initial_grid: grid ANTES do fill
    - start_x, start_y: coordenada inicial
    - delay_ms: tempo entre passos (ms)
    """
    grid = deepcopy(initial_grid)
    rows, cols = len(grid), len(grid[0])

    root = tk.Tk()
    root.title("Flood Fill - Animação")

    canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size)
    canvas.pack()

    rects = [[None]*cols for _ in range(rows)]
    texts = [[None]*cols for _ in range(rows)]

    def draw_cell(i, j):
        v = grid[i][j]
        color = PALETTE.get(v, "#DDDDDD")
        x0, y0 = j*cell_size, i*cell_size
        x1, y1 = x0 + cell_size, y0 + cell_size

        if rects[i][j] is None:
            rects[i][j] = canvas.create_rectangle(
                x0, y0, x1, y1, fill=color, outline="#888888"
            )
            texts[i][j] = canvas.create_text(
                (x0+x1)/2, (y0+y1)/2, text=str(v)
            )
        else:
            canvas.itemconfig(rects[i][j], fill=color)
            canvas.itemconfig(texts[i][j], text=str(v))

    # desenha grid inicial
    for i in range(rows):
        for j in range(cols):
            draw_cell(i, j)

    steps = color_all_regions_steps(grid, start_x, start_y)

    def animate():
        try:
            x, y, color = next(steps)
            draw_cell(x, y)
            root.after(delay_ms, animate)
        except StopIteration:
            # fim da animação
            return

    root.after(400, animate)
    root.mainloop()


# compatibilidade com chamada antiga (sem animação)
def show_gui(grid, cell_size=40):
    rows, cols = len(grid), len(grid[0])
    root = tk.Tk()
    root.title("Flood Fill - Visualização Final")

    canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size)
    canvas.pack()

    for i in range(rows):
        for j in range(cols):
            v = grid[i][j]
            color = PALETTE.get(v, "#DDDDDD")
            x0, y0 = j*cell_size, i*cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#888888")
            canvas.create_text((x0+x1)/2, (y0+y1)/2, text=str(v))

    root.mainloop()
