print("Incluir Datos con Input")
nombre=input("¿Cual es tu nombre? ")
print("!Hola", nombre, "!")
print("Bienvenido a Sprinfield")
print("Hasta luego "+nombre)

cantidad = int(input("¿Cuántas rosquillas hay?"))
total = cantidad +2
print("Rosquillas totales: ", total)

print(" CONVERSIONES ")
print("==== TIENDA DE APU ==========")
nombre_cliente = input("Nombre del cliente: ")
precio = float(input("Precio de Rosquilla: "))
cantidad = int(input("Cantidad: "))
total= cantidad * precio
print("Total a pagar: ", total)
print("Total a pagar (round): ", round(total,2))
print(f"Total a pagar (f): ${total:.2f}")
