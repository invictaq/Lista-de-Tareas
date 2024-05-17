Tareas = ["desayunar", "duchar", "supermercado", "comer"]
print(Tareas)
primerPosicion = Tareas[0]

longitud = len(Tareas)
print(f"El primer valor es:{primerPosicion}\nLalongitud de la lista de Tareas es: {longitud}")

Tareas1 = ["planchar", "limpiar", "cenar"]
print(Tareas1)
ultimaPosicion = Tareas1[-1]
print(ultimaPosicion)


Tareas1 = ["planchar", "limpiar", "cenar"]
palabra = "cenar"
palabra2 = "ginasio"

if palabra in Tareas1:
    print("La palabra pertenece a la Tareas1")

if palabra2 not in Tareas1:
    print("La palabra no está en la Tarea1")

Tareas3 = ["planchar", "limpiar", "cenar", "ginasio"]
print(Tareas3)
Tareas3[1] = "merendar"
print(Tareas3)

Tareas3.remove("ginasio")
print(Tareas3)

Tareas3.append("salir")
print(Tareas3)

Tareas3.pop()
Tareas3.pop(0)
print(Tareas3)

Tareas3.remove("cenar")
print(Tareas3)
print(Tareas3)

elementoEliminado = Tareas3.pop(0)
print(Tareas3)

Tareas3 = ["planchar", "limpiar", "cenar", "ginasio"]
Tareas3.insert(1, "cesta")
print(Tareas3)

Tareas1.extend(Tareas3)
print(Tareas)
print(Tareas3)

Tareas3.extend(Tareas1)
print(Tareas3)

indice = Tareas3.index("cesta")
print(indice)

del Tareas[0]
print(Tareas3)

Fin





























    











































