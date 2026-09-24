import requests as consulta
from model import ModelApi 
from view import ViewApi

class ControllerApi():
    def __init__(self):
        self.modelo = ModelApi()
        self.modelo.consulta_categorias()
        self.modelo.crear_diccionario_categorias()

        self.vista = ViewApi()
        self.vista.mostrar_categorias(self.modelo)
        self.vista.seleccionar_categoria()

    def logica_selenccion(self):
        categoria_seleccionada = None
        for diccionario in self.modelo.lista_categorias_dic:
            if diccionario['clave'] == int(self.vista.seleccion):
                categoria_seleccionada = diccionario['valor']
            
        self.modelo.consulta_jokes(categoria_seleccionada)
        self.vista.mostrar_joke(self.modelo)