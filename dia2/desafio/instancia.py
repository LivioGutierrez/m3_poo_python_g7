from te import Te

te_negro= Te
te_verde= Te

te1=type(te_negro)
te2=type(te_verde)

print(te1)
print(te2)

if te1 == te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
