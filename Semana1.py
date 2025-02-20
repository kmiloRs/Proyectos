from datetime import datetime, timedelta

class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, titulo, descripcion, fecha_vencimiento):
        tarea = {
            'id': len(self.tareas) + 1,
            'titulo': titulo,
            'descripcion': descripcion,
            'fecha_vencimiento': fecha_vencimiento,
            'completada': False
        }
        self.tareas.append(tarea)
        print(f"Tarea '{titulo}' agregada con éxito!")
    
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        
        print("\n=== LISTA DE TAREAS ===")
        for tarea in self.tareas:
            estado = "✓" if tarea['completada'] else " "
            print(f"\nTarea #{tarea['id']}")
            print(f"[{estado}] {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
    
    def marcar_completada(self, id_tarea):
        for tarea in self.tareas:
            if tarea['id'] == id_tarea:
                tarea['completada'] = True
                print(f"Tarea '{tarea['titulo']}' marcada como completada!")
                return
        print("Tarea no encontrada.")
    
    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea['id'] == id_tarea:
                self.tareas.remove(tarea)
                print(f"Tarea #{id_tarea} eliminada con éxito!")
                return
        print("Tarea no encontrada.")
    
    def verificar_vencimientos(self):
        hoy = datetime.now()
        for tarea in self.tareas:
            fecha_venc = datetime.strptime(tarea['fecha_vencimiento'], '%Y-%m-%d')
            dias_restantes = (fecha_venc - hoy).days
            
            if not tarea['completada'] and dias_restantes <= 1:
                print(f"\n¡ALERTA! La tarea '{tarea['titulo']}' vence {fecha_venc.strftime('%Y-%m-%d')}!")

# Ejemplo de uso del programa
def menu_principal():
    gestor = GestorTareas()
    
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Verificar vencimientos")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha de vencimiento (YYYY-MM-DD): ")
            gestor.agregar_tarea(titulo, descripcion, fecha)
        
        elif opcion == "2":
            gestor.mostrar_tareas()
        
        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            gestor.marcar_completada(id_tarea)
        
        elif opcion == "4":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            gestor.eliminar_tarea(id_tarea)
        
        elif opcion == "5":
            gestor.verificar_vencimientos()
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
