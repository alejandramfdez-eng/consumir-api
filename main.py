import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print("categorias: ", categorias.json())
lista_categorias = categorias.json()
print("ultimo dato de lista categorias: ", lista_categorias[len(lista_categorias)-1])

response = consulta.get('https://api.chucknorris.io/jokes/random?category={category*animal}')


print("codigo http de respuesta: ", response.status_code)
print("cabecera: ", response.headers['content-type'])
print("encoding: ", response.encoding)
print("respuesta en string: ", response.text)
print("respuesta en json: ", response.json())