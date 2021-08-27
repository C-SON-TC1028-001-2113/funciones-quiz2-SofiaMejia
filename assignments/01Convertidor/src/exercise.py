# Escribe tus funciones abajo de esta línea
def pies_cm(pies):
    resultado1 = (pies*30.48)
    return(resultado1)

def pulgadas_cm(pulgadas):
    resultado2 = (pulgadas*2.54)
    return(resultado2)

def yardas_cm(yardas): 
    resultado3 = (yardas*91.44)
    return(resultado3)
def main():
    # Escribe tu código abajo de esta línea
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    operacion = str(input('Introduce una opcion: '))
    cantidad = int(input('Introduce la cantidad: '))
    if cantidad > 0 : 
        if operacion == '1': 
            resultado1 = pies_cm(cantidad)
            print(resultado1)
        elif operacion == '2': 
            resultado2 = pulgadas_cm(cantidad)
            print(resultado2)
        elif operacion == '3':
            resultado3 = yardas_cm(cantidad)
            print(resultado3)
        else:
            print('Error')
    else: 
        print('Error')  

if __name__ == '__main__':
    main()
