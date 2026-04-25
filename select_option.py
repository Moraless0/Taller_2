from add_product import registrar_producto

def select_option():
    
    opc = int(input("Ingrese la opcion deseada"))
    

    while True:
        try:
            if opc == 1:
                registrar_producto()
            elif opc == 2:
                print("O2")
            elif opc == 3:
                print("O3")
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
