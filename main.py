import tkinter as tk

root = tk.Tk()

# Define o tamanho da janela
root.geometry("400x400")

# Define o título da janela
root.title("Alarme")

tk.Label(root, text="Definir horário do alarme:", font=('Helvetica 16 bold')).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Define o horário:
opt = tk.StringVar()
options = ['0', '1', '2', '3']
opt.set(options[0])

tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)




root.mainloop()