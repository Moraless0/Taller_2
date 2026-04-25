import json

def actualizar_cantidad():
    try:
        with open("productos.json", "r") as f:
            productos = json.load(f)
    except:
        print("No hay productos registrados.")
        return

    nombre = input("Nombre del producto: ")

    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
    except:
        print("Cantidad inválida.")
        return

    encontrado = False

    for p in productos:
        if p.get("nombre", "").lower() == nombre.lower():
            p["cantidad"] = nueva_cantidad
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")
        return

    with open("productos.json", "w") as f:
        json.dump(productos, f, indent=4)

    print("Cantidad actualizada ✅")