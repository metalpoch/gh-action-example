nombre    =    "Mundo"
contador=0
frutas = [   "manzana","banana",      "pera",     "uva"   ]




print(   "Hola,   "+nombre   +"!"   )
print("Este programa tiene variables y bucles")


for   fruta    in    frutas:
        print("Fruta numero "+str(contador+1)+": "+fruta)
        contador   =   contador   +   1



while contador>0:
    print("Cuenta regresiva: "+str(contador))
    contador-=1



print("Fin del programa")

suma=0
for i in range(1,11):
            suma=suma+i
print("La suma del 1 al 10 es: "+str(suma))




def saludar(nombre):
    return    "Hola, "+nombre+" desde una funcion"



print(saludar("Python"))
