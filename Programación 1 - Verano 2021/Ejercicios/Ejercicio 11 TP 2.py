# Resolver el siguiente problema, diseñando las funciones a utilizar:
# Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción indicando
# su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con turno
# (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:
# a.Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden
# que llegaron a la clínica.
# b.Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.
# Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

# Funciones: 

def cargarlista(pac,aten,l1,l2): #Función para cargar las listas
    """ Carga las listas de
    pacientes y servicios """
    l1.append(pac)
    l2.append(aten)
    
def imprimirlista(l1,l2):
    """ Imprime las listas separadas entre urgencias
    y turnos """
    print("Listado de pacientes atendidos por urgencias: ")
    for i in range (len(l2)):
        if l2[i] == 0:  # Imprime urgencias
            print(l1[i],end=" ")
    print()        
    print("Lista de pacientes atendidos por turno: ")
    for i in range(len(l2)):
        if l2[i] == 1:  # Imprime turnos
            print(l1[i],end=" ")
    print()

def busqueda(pac,l1,l2):
    """ Busca un paciente y devuelve la cantidad de veces que se
    atendio por urgencias asi como por turnos """
    inicio=0
    largo=len(l1)
    urg=0
    tur=0
    while pac in l1[inicio:largo]:
        ubicacion = l1.index(pac,inicio)
        servicio=l2[ubicacion]
        if servicio==0:
            urg += 1
        else:
            tur += 1
        inicio = ubicacion + 1
    return urg , tur
    
# Programa principal:

totalpacientes = []
totalservicios = []

paciente = int(input("Ingrese el número de afiliado de 4 digitos: "))
while paciente != -1:
    if paciente != -1:
        servicio = int(input("Ingrese 0 si es urgencia / 1 si es con turno : "))
        cargarlista(paciente,servicio,totalpacientes,totalservicios)
    paciente = int(input("Ingrese el número de afiliado de 4 digitos: "))

print(totalpacientes)
print(totalservicios)

imprimirlista(totalpacientes, totalservicios)

paciente = int(input("Ingrese el número de afiliado del que desea buscar su historial de atención o ingrese -1 para finalizar: "))
while paciente != -1:
    urgencias , turnos = busqueda(paciente,totalpacientes,totalservicios)
    print("El paciente",paciente,"se atendió",urgencias,"veces por urgencias y",turnos,"veces por turnos")
    paciente = int(input("Ingrese el número de afiliado del que desea buscar su historial de atención o ingrese -1 para finalizar: "))

