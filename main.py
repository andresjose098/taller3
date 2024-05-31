from view.parqueadero_view import ParqueaderoView
from controller.parqueadero_controller import ParqueaderoController
from model.parqueadero_model import ParqueaderoModel

if __name__ == '__main__':
    model = ParqueaderoModel()
    view = ParqueaderoView()
    controller = ParqueaderoController(model, view)
    view.set_controller(controller)
    view.main_loop()
