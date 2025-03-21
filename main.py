import tkinter as tk
import time
import pygame
from threading import Thread
from tkinter import messagebox

# Caminho do arquivo de áudio 
MUSICA = r"D:\Free_Tracks\EFEITOS SONOROS-20211122T191053Z-001\EFEITOS SONOROS\Sound Effects Pack - 2\KEVIN MACLEOD MOVEMENT PROPOSITION.mp3" 

# Inicializa o mixer do pygame
pygame.mixer.init()

def tocar_alarme():
    """Toca a música repetidamente até o usuário parar."""
    pygame.mixer.music.load(MUSICA)
    pygame.mixer.music.play(-1)  # Loop infinito

def parar_alarme():
    """Para a música do alarme."""
    pygame.mixer.music.stop()

def verificar_alarme():
    """Verifica continuamente se o horário do alarme foi atingido."""
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = time.strftime("%H:%M:%S")
        
        if current_time == set_alarm_time:
            tocar_alarme()
            messagebox.showinfo("Alarme", "⏰ Hora do alarme! Para parar, clique no botão.")
            break

        time.sleep(1)

def iniciar_verificacao():
    """Inicia a verificação do alarme em uma nova thread para não travar a interface."""
    Thread(target=verificar_alarme, daemon=True).start()


# Criando a janela no tkinter
root = tk.Tk()

# Define o tamanho da janela
root.geometry("400x300")

# Define o título da janela
root.title("Alarme")

tk.Label(root, text="Definir horário do alarme:", font=('Helvetica 16 bold')).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Define o horário:
def option(value):
    opt = tk.StringVar()
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)
    
tk.Button(root, text="Definir Alarme", font=('Helvetica', 12), command=iniciar_verificacao).pack(pady=10)
tk.Button(root, text="Parar Alarme", font=('Helvetica', 12), command=parar_alarme).pack(pady=10)




root.mainloop()