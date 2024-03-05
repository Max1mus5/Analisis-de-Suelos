import tkinter as tk
from tkinter import ttk

def mostrar_tabla(data, mediana_edaficas):
    # Crear ventana
    ventana = tk.Tk()
    ventana.geometry("800x400")
    ventana.title("Información de cultivos")

    # Crear encabezado
    encabezado = tk.Label(ventana, text="Información de cultivos", font=("Arial", 18))
    encabezado.pack()

    # Crear Frame para tabla
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(expand=True, fill="both")

    # Crear Scrollbars
    scrollbar_vertical = tk.Scrollbar(frame_tabla, orient="vertical")
    scrollbar_horizontal = tk.Scrollbar(frame_tabla, orient="horizontal")

    # Configurar Scrollbars
    scrollbar_vertical.pack(side="right", fill="y")
    scrollbar_horizontal.pack(side="bottom", fill="x")

    # Crear tabla
    tabla = ttk.Treeview(frame_tabla, yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Configurar Scrollbars para la tabla
    scrollbar_vertical.config(command=tabla.yview)
    scrollbar_horizontal.config(command=tabla.xview)

    # Encabezados de columna
    tabla["columns"] = ("Departamento", "Municipio", "Cultivo", "Topología")
    tabla.heading("#0", text="Índice")
    tabla.column("#0", width=50, minwidth=50, anchor="center")
    tabla.heading("Departamento", text="Departamento")
    tabla.heading("Municipio", text="Municipio")
    tabla.heading("Cultivo", text="Cultivo")
    tabla.heading("Topología", text="Topología")

    # Insertar datos en la tabla
    for i, row in data.iterrows():
        tabla.insert("", "end", text=i+1, values=(row["departamento"], row["municipio"], row["cultivo"], row["topografia"]))

    # Alinear contenido de celdas
    for col in tabla["columns"]:
        tabla.column(col, anchor="center")

    # Empacar la tabla
    tabla.pack(expand=True, fill="both")

    etiqueta_mediana = tk.Label(ventana, text="Mediana de variables edáficas:", font=("Arial", 12))
    etiqueta_mediana.pack()

    tabla_mediana = tk.Frame(ventana)
    tabla_mediana.pack()

    etiqueta_variable = tk.Label(tabla_mediana, text="Variable", font=("Arial", 10))
    etiqueta_variable.grid(row=0, column=0)
    etiqueta_mediana_valor = tk.Label(tabla_mediana, text="Mediana", font=("Arial", 10))
    etiqueta_mediana_valor.grid(row=0, column=1)

    fila = 1
    for variable, mediana in mediana_edaficas.items():
        etiqueta_variable = tk.Label(tabla_mediana, text=variable, font=("Arial", 10))
        etiqueta_variable.grid(row=fila, column=0)
        etiqueta_mediana_valor = tk.Label(tabla_mediana, text=mediana, font=("Arial", 10))
        etiqueta_mediana_valor.grid(row=fila, column=1)
        fila += 1

    # Bucle para mantener la ventana abierta
    ventana.mainloop()
