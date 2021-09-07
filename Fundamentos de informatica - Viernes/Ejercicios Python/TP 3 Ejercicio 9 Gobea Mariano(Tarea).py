NumeroBinario=int(input("Ingrese un numero binario de 4 dígitos: "))
Unidad=NumeroBinario%10
NumeroBinario_1=NumeroBinario//10
Decena=NumeroBinario_1%10
NumeroBinario_2=NumeroBinario_1//10
Centena=NumeroBinario_2%10
NumeroBinario_3=NumeroBinario_2//10
UnidadDeMil=NumeroBinario_3%10
NumeroDecimal=(Unidad*2**0)+(Decena*2**1)+(Centena*2**2)+(UnidadDeMil*2**3)
print("Su equivalente en numeros decimales es: ",NumeroDecimal)



