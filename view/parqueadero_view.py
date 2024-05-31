# view/parqueadero_view.py
from tkinter import *
from tkinter import messagebox


class ParqueaderoView:
    def __init__(self):
        self.root = Tk()
        self.root.title("Gestión de Parqueadero")
        self.controller = None

        self.frame_input = Frame(self.root)
        self.frame_input.pack(pady=20)

        self.label = Label(self.frame_input, text="Placa del Vehículo:")
        self.label.pack(side=LEFT)

        self.entry_vehicle = Entry(self.frame_input)
        self.entry_vehicle.pack(side=LEFT)

        self.add_button = Button(self.frame_input, text="Añadir Vehículo", command=self.add_vehicle)
        self.add_button.pack(side=LEFT)

        self.release_button = Button(self.frame_input, text="Liberar Vehículo", command=self.release_vehicle)
        self.release_button.pack(side=LEFT)

        self.frame_display = Frame(self.root)
        self.frame_display.pack(pady=20)

    def set_controller(self, controller):
        self.controller = controller

    def add_vehicle(self):
        vehiculo = self.entry_vehicle.get()
        self.controller.add_vehicle(vehiculo)

    def release_vehicle(self):
        vehiculo = self.entry_vehicle.get()
        self.controller.release_vehicle(vehiculo)

    def refresh_display(self, espacios):
        for widget in self.frame_display.winfo_children():
            widget.destroy()
        for espacio in espacios:
            estado = f"Espacio {str(espacio['_id'])[-4:]}: {'Ocupado por ' + espacio['vehiculo'] if espacio['ocupado'] else 'Libre'}"
            Label(self.frame_display, text=estado).pack()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def main_loop(self):
        self.root.mainloop()
