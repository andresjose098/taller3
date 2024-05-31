# controller/parqueadero_controller.py

class ParqueaderoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.inicializar_espacios()
        self.refresh_display()

    def add_vehicle(self, vehiculo):
        if self.model.ocupar_espacio(vehiculo):
            self.view.refresh_display(self.model.obtener_espacios())
        else:
            self.view.show_error("No hay espacios disponibles")

    def release_vehicle(self, vehiculo):
        if self.model.liberar_espacio(vehiculo):
            self.view.refresh_display(self.model.obtener_espacios())
        else:
            self.view.show_error("Vehículo no encontrado")

    def refresh_display(self):
        espacios = self.model.obtener_espacios()
        self.view.refresh_display(espacios)
