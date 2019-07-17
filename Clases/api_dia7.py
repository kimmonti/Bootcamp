import requests

KEY = "7cbdf22d"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Interstellar"

def director(title):
    busqueda = URL + KEY + "&t=" + title
    print(busqueda)
    resultado = requests.get(busqueda)
    return resultado.json()["Director"] #Json convierte la info a diccionario

print("El nombre del director de la pelicula es", director("The martian"))
print("El nombre del director de la pelicula es", director("Harry Potter"))
print("El nombre del director de la pelicula es", director("Interstellar"))