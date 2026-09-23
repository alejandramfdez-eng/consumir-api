lista =['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
lista_diccionario = []
num = 0
for i in lista:
    print(i)
    num = num + 1
    lista_diccionario.append({'clave': num, 'valor': i})#agregar un diccionario por cada vuelta a mi lista

print(lista_diccionario)

for diccionario in lista_diccionario:
    print(f"{diccionario['clave']} - {diccionario['valor']}")

seleccion = input("Seleccione un numero para categoría: ")

for diccionario in lista_diccionario:
    if diccionario['clave'] == int(seleccion):
        print(f"Tu seleccion fue: {diccionario['valor']}")
       