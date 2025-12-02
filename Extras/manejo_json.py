import json

json_string = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'

print (f"Tipo original: {type(json_string)}")

pyton_dict = json.loads(json_string)

print (f"Dato convertido: {pyton_dict}")
print (f"Tipo nuevo: {type(pyton_dict)}")

print (f"Accediendo al nombre: {pyton_dict['nombre']}")
print (f"Accediendo a la edad: {pyton_dict['edad']}")

datos_python = {
    "canal": "JulioProfe",
    "autor": "Julio Rios",
    "subs": 1500,
    "frameworks_favoritos": ["React", "Vue", "Angular", "Svelte"]
}

json_data = json.dumps(datos_python)
print (f"El string JSON: {json_data}")
print (f"Tipo: {type(json_data)}")

json_indentado = json.dumps(datos_python, indent=4, sort_keys=True)
print ("--- JSON Indentado y Ordenado ---")
print (json_indentado)

encoder = json.JSONEncoder()
json_encoded = encoder.encode({"lenguajes": ["Python", "JavaScript", "Rust"]})

print (f"Codificado:{json_encoded}")

decoder = json.JSONDecoder()
json_decoded = decoder.decode(json_encoded)
print (f"Decodificado: {json_decoded}")
print (f"Tipo decodificado: {type(json_decoded)}")

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("001", "Laptop Gamer", 1499.99)

print (f"Objeto original: {producto1}")

json_objeto = json.dumps(producto1.__dict__, indent=2)

print ("--- JSON del Objeto ---")
print (json_objeto)
print (f"Tipo del JSON: {type(json_objeto)}")

dict_desde_json = json.loads(json_objeto)

print ("\n--- Diccionario desde JSON ---")
print (dict_desde_json)
print (f"Tipo del diccionario: {type(dict_desde_json)}")