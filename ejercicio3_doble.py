import os

#BOLETA DE VENTA
#declarar variables
cliente,pantalon,camisa,polo,precio_pantalon,precio_camisa,precio_polo="","","","",0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
pantalon=os.sys.argv[2]
camisa=os.sys.argv[3]
polo=os.sys.argv[4]
precio_pantalon=float(os.sys.argv[5])
precio_camisa=float(os.sys.argv[6])
precio_polo=float(os.sys.argv[7])

# PROCESSING
total=(precio_pantalon+precio_camisa+precio_polo)

# VERIFICADOR
ganancia=(total<1)

#OUTPUT
print("#########################")
print("# centro:    caballero ")
print("#########################")
print("# cliente:", cliente)
print("# pantalon:", pantalon,"precio:   S/.", precio_pantalon)
print("# camisa:", camisa,"precio:   S/.", precio_camisa)
print("# polo:", polo,"precio:   S/.", precio_polo)
print("# total:   S/.", total)
print("#########################")
print("# ganancia obtenida:", ganancia)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 800.00, ganaste un bale un polo por la compra
if( total>630):
    print("Ud ha ganado un polo por la compra")
else:
    print("Ud no ganado un polo por la compra")
# fin_if