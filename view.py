class ViewApi():
    def __init__(self):
        self.selenccion = None

    def mostrar_categorias(self, modelo):
        for diccionario in modelo.lista_categorias_dic:
            print(f"{diccionario['clave']} - {diccionario['valor']}")

    def seleccionar_categoria(self):
        self.seleccion = int(input("Seleccione un numero para categoría: ") )

    def mostrar_joke(self, modelo):
        print("respuesta en json: ", modelo.jokes.json())
        