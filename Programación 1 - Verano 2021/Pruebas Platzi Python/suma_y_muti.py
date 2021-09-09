def run ():        #Le sume maneje de errores con try y except
    next=True
    while next:    
        try:    
            numero1=float(input("Ingrese el primer número que desea sumar: "))
            numero2=float(input("Ingrese el segundo número que desea sumar: "))
            numero3=float(input("Ingrese el tercer número. Este se multiplicara: "))
            suma=round((numero1+numero2)*numero3,2)
            print("El resultado es: "+str(suma)+". Gracias por usar nuestro servio. Vuelva pronto")
            next=False
        except ValueError as VE:
            print("Recuerde que solo debe ingresar numeros y el indicador de decimales es el punto. No la coma")

if __name__ == '__main__':
    run()