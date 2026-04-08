import tkinter as tk
from tkinter import colorchooser

# Configuração inicial
janela = tk.Tk()
janela.title("🎨 Paint Luiz Felipe")
janela.configure(bg="#2c2f33")

cor_atual = "#ffffff"
x_ant, y_ant = None, None

def iniciar_desenho(event):
    global x_ant, y_ant
    x_ant, y_ant = event.x, event.y

def desenhar(event):
    global x_ant, y_ant
    canvas.create_line(x_ant, y_ant, event.x, event.y,
                       fill=cor_atual, width=espessura.get(),
                       capstyle=tk.ROUND, smooth=True)
    x_ant, y_ant = event.x, event.y

def escolher_cor():
    global cor_atual
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_atual = cor

def limpar_canvas():
    canvas.delete("all")

# Canvas com estilo
canvas = tk.Canvas(janela, bg="#23272a", width=800, height=500, highlightthickness=0)
canvas.pack(padx=20, pady=20)
canvas.bind("<Button-1>", iniciar_desenho)
canvas.bind("<B1-Motion>", desenhar)

# Frame de controles
frame = tk.Frame(janela, bg="#2c2f33")
frame.pack(pady=10)

estilo_botao = {
    "bg": "#7289da",
    "fg": "#ffffff",
    "activebackground": "#99aab5",
    "activeforeground": "#ffffff",
    "font": ("Segoe UI", 10, "bold"),
    "bd": 0,
    "padx": 10,
    "pady": 5
}

btn_cor = tk.Button(frame, text="Escolher Cor 🎨", command=escolher_cor, **estilo_botao)
btn_cor.grid(row=0, column=0, padx=10)

btn_limpar = tk.Button(frame, text="Limpar Tela 🧹", command=limpar_canvas, **estilo_botao)
btn_limpar.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Espessura:", bg="#2c2f33", fg="#ffffff", font=("Segoe UI", 10)).grid(row=0, column=2, padx=10)
espessura = tk.Scale(frame, from_=1, to=15, orient=tk.HORIZONTAL, bg="#2c2f33", fg="#ffffff",
                     troughcolor="#99aab5", highlightthickness=0)
espessura.set(5)
espessura.grid(row=0, column=3)

janela.mainloop()
