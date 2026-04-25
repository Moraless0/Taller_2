from show_menu import show_menu

from add_product import registrar_producto
from edit_products import actualizar_cantidad
from show_products import listar_productos

def select_option():

    while True:
        show_menu()

        try:
            opc = int(input("Ingrese la opcion deseada: "))

            if opc == 1:
                registrar_producto()

            elif opc == 2:
                actualizar_cantidad()

            elif opc == 3:
                listar_productos()

            elif opc == 4:
                print("Saliendo...")
                break

            else:
                print("❌ Opción inválida")

        except Exception:
            print("❌ Error, ingrese un número válido")