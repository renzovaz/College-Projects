print("1. Conversão de Fahrenheit para Celsius")
print("Fahrenheit | Celsius")
for f in range(45, 81):
    c = (5 * (f - 32)) / 9
    print(f"{f:.1f} °F | {c:.3f} °C")
print("\n")