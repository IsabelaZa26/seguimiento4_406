# === Clase Vendedor con validación de edad e interfaz gráfica ===
import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.verificar_edad(edad)
        self.edad = edad

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        elif edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        else:
            return True

    def imprimir(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"

# === Funciones para la interfaz ===
def crear_vendedor():
    try:
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = int(entry_edad.get())

        vendedor = Vendedor(nombre, apellidos, edad)
        messagebox.showinfo("Vendedor creado", vendedor.imprimir())
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

# === Interfaz ===
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("300x250")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellidos:").pack(pady=5)
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Registrar", command=crear_vendedor).pack(pady=10)
tk.Button(ventana, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()

