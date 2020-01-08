import os

# BOLETA DE VENTA
# declarar variables
cliente,auto1,auto2,precio_auto1,precio_auto2="","","",0.0,0.0

# INPUT
cliente=os.sys.argv[1]
auto1=os.sys.argv[2]
auto2=os.sys.argv[3]
precio_auto1=float(os.sys.argv[4])
precio_auto2=float(os.sys.argv[5])

# PROCESSING
total=(precio_auto1+precio_auto2)

# VERIFICADOR
ganancia_vendedor=(total==100000)

#OUTPUT
print("#########################")
print("# SAC. TOYOTA-PERU")
print("#########################")
print("# cliente:", cliente)
print("# carro:", auto1," precio:  S/.", precio_auto1)
print("# carro:", auto2,"precio:  S/.", precio_auto2)
print("total:    S/.", total)
print("#########################")
print("# ganancia del vendedor:", ganancia_vendedor)
print("#########################")

# CONDICIONAL DOBLE
# si el total es mayor a S/. 800 000.00,conpraste auto de lujo
if( total>800000):
    print("ud ha conprado el auto de lujo")
else:
    print("Ud no ha comprado el auto de lujo")
# fin_if
