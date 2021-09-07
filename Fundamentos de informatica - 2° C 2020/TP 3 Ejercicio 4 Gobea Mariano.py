SalarioBase=50000
Comisión=2500
Vendedor=int(input("Ingrese el numero de vendedor: "))
QVentas=int(input("Ingrese la cantidad de ventas realizadas en el mes por el vendedor en cuestión: "))
TotalVentas=float(input("Ingrese el monto total de las ventas realizadas por el vendedor en cuestión: "))
print("El vendedor N°",Vendedor,"debe cobrar un salario de $:",SalarioBase+(Comisión*QVentas)+(TotalVentas*5/100))
