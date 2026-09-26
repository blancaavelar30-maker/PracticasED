def calcular_salario_neto(salario_bruto: float, porcentaje_impuestos: float)-> float:

    salario_neto = salario_bruto - (salario_bruto * porcentaje_impuestos)
    return salario_neto

salario = float(input("Introduce tu salario bruto:"))
impuesto = float(input("Introduce el porsentaje de impuestos( 0.16):"))

resultado = calcular_salario_neto(salario, impuesto)
print(f"Tu salario neto es: {resultado}")


