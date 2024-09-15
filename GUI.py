import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entrada.get()
    if info:
        lista.insert(tk.END, info)
        entrada.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista y el campo de texto
def limpiar_info():
    lista.delete(0, tk.END)
    entrada.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Información")
ventana.geometry("400x300")

# Etiqueta para el campo de texto
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Campo de texto para ingresar información
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Botón para agregar información a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

# Lista para mostrar la información añadida
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Botón para limpiar la lista y el campo de texto
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()