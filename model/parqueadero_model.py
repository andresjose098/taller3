# model/parqueadero_model.py
from pymongo import MongoClient


class ParqueaderoModel:
    def __init__(self):
        # Conectar a MongoDB
        self.client = MongoClient('mongodb+srv://felipemolina:admin@edya2.zgsyghc.mongodb.net/proyectoInformatico')
        self.db = self.client['parqueadero']
        self.coleccion_espacios = self.db['espacios']

    def inicializar_espacios(self):
        # Asegurarse de que haya 20 espacios al inicio
        if self.coleccion_espacios.count_documents({}) == 0:
            for i in range(20):
                self.coleccion_espacios.insert_one({'ocupado': False, 'vehiculo': None})

    def ocupar_espacio(self, vehiculo):
        espacio = self.coleccion_espacios.find_one({'ocupado': False})
        if espacio:
            resultado = self.coleccion_espacios.update_one({'_id': espacio['_id']}, {'$set': {'vehiculo': vehiculo, 'ocupado': True}})
            return resultado.modified_count > 0
        return False

    def liberar_espacio(self, vehiculo):
        resultado = self.coleccion_espacios.update_one({'vehiculo': vehiculo}, {'$set': {'vehiculo': None, 'ocupado': False}})
        return resultado.modified_count > 0

    def obtener_espacios(self):
        return list(self.coleccion_espacios.find({}))
