print("Comporbador de elegibilidad 101")

nombre = input("Por favor, introduzca su nombre: ")
edad = int(input("Por favor, introduzca su edad: "))
salario = int(input("¿Cuál es su salario mensual?: "))
min_salario = 5000
tiene_buen_credito = False
if not salario >= min_salario or tiene_buen_credito:
    print(f"Felicitaciones {nombre}, Usted es elegible para una hipoteca.")
else:
    print(f"{nombre}, parece que no puede ser elegible en este momento")
