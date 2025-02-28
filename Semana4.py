import time
import random
import tkinter as tk
from tkinter import messagebox, ttk

class Vehiculo:
    def __init__(self, modelo, matricula, año, capacidad, estado, velocidad_maxima, fecha_mantenimiento):
        self.modelo = modelo
        self.matricula = matricula
        self.año = año
        self.capacidad = capacidad
        self.estado = estado
        self.velocidad_maxima = velocidad_maxima
        self.fecha_mantenimiento = fecha_mantenimiento
        self.kilometraje = 0
        self.alerta = ""

    def actualizar_kilometraje(self, km):
        self.kilometraje += km

    def verificar_mantenimiento(self):
        return time.time() > self.fecha_mantenimiento

    def verificar_velocidad(self, velocidad_actual):
        return velocidad_actual > self.velocidad_maxima

class SistemaFlota:
    def __init__(self, app):
        self.vehiculos = []
        self.app = app

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def monitorear_vehiculos(self):
        for vehiculo in self.vehiculos:
            velocidad_actual = random.randint(50, 120)
            vehiculo.actualizar_kilometraje(10)
            vehiculo.alerta = ""

            if vehiculo.verificar_velocidad(velocidad_actual):
                vehiculo.alerta += f"Exceso de velocidad ({velocidad_actual} km/h). "

            if vehiculo.verificar_mantenimiento():
                vehiculo.alerta += "Necesita mantenimiento. "

        self.app.actualizar_tabla()
        self.app.after(5000, self.monitorear_vehiculos)

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Monitoreo de Flota")
        self.geometry("800x400")
        self.sistema = SistemaFlota(self)
        self.crear_widgets()
        self.iniciar_vehiculos()

    def crear_widgets(self):
        self.tabla = ttk.Treeview(self, columns=("Modelo", "Matrícula", "Año", "Capacidad", "Estado", "Vel. Máx", "Alerta"), show="headings")
        self.tabla.heading("Modelo", text="Modelo")
        self.tabla.heading("Matrícula", text="Matrícula")
        self.tabla.heading("Año", text="Año")
        self.tabla.heading("Capacidad", text="Capacidad (kg)")
        self.tabla.heading("Estado", text="Estado")
        self.tabla.heading("Vel. Máx", text="Vel. Máx (km/h)")
        self.tabla.heading("Alerta", text="Alerta")

        self.tabla.column("Modelo", width=100)
        self.tabla.column("Matrícula", width=100)
        self.tabla.column("Año", width=80)
        self.tabla.column("Capacidad", width=120)
        self.tabla.column("Estado", width=100)
        self.tabla.column("Vel. Máx", width=100)
        self.tabla.column("Alerta", width=200)

        self.tabla.pack(fill=tk.BOTH, expand=True)

    def iniciar_vehiculos(self):
        vehiculo1 = Vehiculo("Camión A", "ABC123", 2020, 1000, "Bueno", 80, time.time() + 10)
        vehiculo2 = Vehiculo("Camión B", "XYZ789", 2019, 1200, "Bueno", 90, time.time() + 15)

        self.sistema.agregar_vehiculo(vehiculo1)
        self.sistema.agregar_vehiculo(vehiculo2)

        self.sistema.monitorear_vehiculos()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for vehiculo in self.sistema.vehiculos:
            self.tabla.insert("", tk.END, values=(
                vehiculo.modelo,
                vehiculo.matricula,
                vehiculo.año,
                vehiculo.capacidad,
                vehiculo.estado,
                vehiculo.velocidad_maxima,
                vehiculo.alerta
            ))

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()