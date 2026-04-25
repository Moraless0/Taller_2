import json

def listar_productos():
    try:
        with open("productos.json", "r") as f:
            productos = json.load(f)
    except:
        print("No hay productos registrados.")
        return

    if not productos:
        print("No hay productos registrados.")
        return

    print("\nInventario de productos\n")

    for i, p in enumerate(productos, 1):
        print(f"{i}. {p.get('nombre', 'Sin nombre')}")
        print(f"Precio: {p.get('precio', 0)}")
        print(f"Cantidad: {p.get('cantidad', 0)}\n")