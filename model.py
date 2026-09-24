import requests as consulta

class ModelApi:
    def __init__(self):
        self.categorias = None
        self.jokes = None
        self.lista_categorias = []
        self.lista_categorias_dic = []

    def consulta_categorias(self):
        self.categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
        self.lista_categorias = self.categorias.json()

    def consulta_jokes(self, categoria_seleccionada):
        self.jokes = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

    def crear_diccionario_categorias(self):
        num = 0
        for i in self.lista_categorias:
            num = num + 1
            self.lista_categorias_dic.append({'clave': num, 'valor': i})#agregar un diccionario por cada vuelta a mi lista