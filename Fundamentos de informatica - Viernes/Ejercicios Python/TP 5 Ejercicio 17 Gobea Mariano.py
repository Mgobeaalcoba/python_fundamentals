usuario=input("Ingrese su usuario: ")
contador=1
while usuario!="admin" and contador<3:   
    usuario=input("Usuario incorrecto. Ingrese su usuario: ")
    if usuario!="admin":
        contador=contador+1 
if contador==3:
    print("Se agotaron los 3 intentos de validación.")
elif usuario=="admin":
    contraseña=input("Ingrese su contraseña: ")
    while contraseña!="1234" and contador<3:        
        contraseña=input("Contraseña incorrecta. Ingrese su contraseña: ")
        if contraseña!="1234":
            contador=contador+1 
    if contador==3:
        print("Se agotaron los 3 intentos de validación.")
    elif contraseña=="1234":
        print("Login exitoso")
    


