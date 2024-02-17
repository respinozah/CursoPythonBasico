
salarioBruto = int(input("Ingrese el salario bruto: "))

cargasSociales = salarioBruto * (9 / 100)
asociacionSolidarista = salarioBruto * (5 / 100)
salarioNeto = salarioBruto - (cargasSociales + asociacionSolidarista)
print(f"El salario neto es: {salarioNeto}")

porcentajeBono = int(input("Especificar bonificacion por rendimiento: "))
salarioNeto = salarioNeto + (salarioBruto * (porcentajeBono/100))
print(f"Salario neto mas bonificacion por rendimiento es: {salarioNeto}")
