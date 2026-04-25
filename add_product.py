import json

def registrar_producto():
    nombre = input("Nombre del producto: ").lower()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    try:
        with open("productos.json", "r") as f:
            productos = json.load(f)
    except:
        productos = []

    productos.append(producto)

    with open("productos.json", "w") as f:
        json.dump(productos, f, indent=4)

    print("Producto guardado ✅")