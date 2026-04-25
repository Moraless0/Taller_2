from show_menu import show_menu

from add_product import registrar_producto
from edit_products import actualizar_cantidad
from show_products import listar_productos

def select_option():

    show_menu()

    opc = int(input("Ingrese la opcion deseada"))
    

    while True:
        try:
            if opc == 1:
                registrar_producto()
            elif opc == 2:
                actualizar_cantidad()
            elif opc == 3:
                listar_productos()
            elif opc == 4:
                print("O4")
            elif opc == 5:
                print("O5")
            elif opc == 6:
                print("O6")
                break
            else:
                print("Invalido")
        
        except Exception:
            print("Error")
