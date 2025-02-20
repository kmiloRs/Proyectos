from datetime import datetime

class Visitante:
    def __init__(self, nombre, documento, tipo):
        self.nombre = nombre
        self.documento = documento
        self.tipo = tipo
        self.fecha_registro = datetime.now()

class ControlAcceso:
    def __init__(self):
        self.visitantes = []
        self.registros = []
        
    def registrar_visitante(self, nombre, documento, tipo):
        visitante = Visitante(nombre, documento, tipo)
        self.visitantes.append(visitante)
        return visitante
    
    def registrar_entrada(self, documento):
        visitante = self.buscar_visitante(documento)
        if visitante:
            registro = {
                "visitante": visitante,
                "tipo": "entrada",
                "fecha": datetime.now()
            }
            self.registros.append(registro)
            return "Entrada registrada para " + visitante.nombre
        return "Visitante no encontrado"
    
    def registrar_salida(self, documento):
        visitante = self.buscar_visitante(documento)
        if visitante:
            registro = {
                "visitante": visitante,
                "tipo": "salida",
                "fecha": datetime.now()
            }
            self.registros.append(registro)
            return "Salida registrada para " + visitante.nombre
        return "Visitante no encontrado"
    
    def buscar_visitante(self, documento):
        for visitante in self.visitantes:
            if visitante.documento == documento:
                return visitante
        return None
    
    def ver_registros_del_dia(self):
        hoy = datetime.now().date()
        registros_hoy = []
        
        for registro in self.registros:
            if registro["fecha"].date() == hoy:
                registros_hoy.append({
                    "nombre": registro["visitante"].nombre,
                    "tipo": registro["tipo"],
                    "hora": registro["fecha"].strftime("%H:%M")
                })
        
        return registros_hoy
        
sistema = ControlAcceso()

print("Registrando visitantes...")
sistema.registrar_visitante("Juan Pérez", "12345", "empleado")
sistema.registrar_visitante("Ana García", "67890", "visitante")

print("\nRegistrando movimientos...")
print(sistema.registrar_entrada("12345"))
print(sistema.registrar_salida("67890"))

print("\nRegistros del día:")
registros = sistema.ver_registros_del_dia()
for registro in registros:
    print(f"{registro['nombre']} - {registro['tipo']} - {registro['hora']}")
