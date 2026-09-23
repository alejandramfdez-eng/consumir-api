import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
#print("categorias: ", categorias.json())
lista_categorias = categorias.json()
lista_categorias_dic = []
num = 0
for i in lista_categorias:
    print(i)
    num = num + 1
    lista_categorias_dic.append({'clave': num, 'valor': i})#agregar un diccionario por cada vuelta a mi lista

for diccionario in lista_categorias_dic:
    print(f"{diccionario['clave']} - {diccionario['valor']}")

seleccion = int(input("Seleccione un numero para categoría: ") )
categoria_seleccionada = None

for diccionario in lista_categorias_dic:
    if diccionario['clave'] == int(seleccion):
        categoria_seleccionada = diccionario['valor']
        #print(f"Tu seleccion fue: {diccionario['valor']}")

#print("ultimo dato de lista categorias: ", lista_categorias[len(lista_categorias)-1])

response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')


#print("codigo http de respuesta: ", response.status_code)
#print("cabecera: ", response.headers['content-type'])
#print("encoding: ", response.encoding)
#print("respuesta en string: ", response.text)
print("respuesta en json: ", response.json())

['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 
 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 
 'science', 'sport', 'travel']