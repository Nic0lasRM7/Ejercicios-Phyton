SalarioBase = float(input("Ingres su salario base"))
AportePension = SalarioBase * 0.04
aporteSeguridadsocial = SalarioBase * 0.04
salarioNeto = SalarioBase - aporteSeguridadsocial - AportePension

print(f"Su aporte a la seguridad social es: {aporteSeguridadsocial}")
print(f"Su aporte a la pension es: {AportePension}")
print(f"Su salario Neto es: {salarioNeto}")
