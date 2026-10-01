def calcular_presion(moles, temperatura_k, volumen_l):
    # Constante universal de los gases ideales (L·atm / K·mol)
    R = 0.0821 
    presion = (moles * R * temperatura_k) / volumen_l
    return presion

print("Cálculo de Presión - Gas Ideal")
n = float(input("Ingrese el número de moles (n): "))
t = float(input("Ingrese la temperatura en Kelvin (K): "))
v = float(input("Ingrese el volumen en Litros (V): "))

p = calcular_presion(n, t, v)
print(f"La presión calculada es: {p:.2f} atm")
0

