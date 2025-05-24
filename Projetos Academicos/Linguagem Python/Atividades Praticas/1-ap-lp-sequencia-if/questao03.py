# Coeficientes do plano P: Ax + By + Cz + D1 = 0
A1 = 2
B1 = -3
C1 = 4
D1 = -5

# Coeficientes do plano Q: Ax + By + Cz + D2 = 0
A2 = 2
B2 = -3
C2 = 4
D2 = 7

# Verificar se os planos são paralelos
if (A1 * B2 == A2 * B1) and (A1 * C2 == A2 * C1) and (B1 * C2 == B2 * C1):
    numerador = abs(D1 - D2)
    denominador = (A1**2 + B1**2 + C1**2) ** 0.5  # raiz quadrada sem math
    distancia = numerador / denominador
    print("Distância entre os planos:", round(distancia, 2))
else:
    print("Os planos não são paralelos, então a distância é 0.")