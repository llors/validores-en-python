import os

# BOLETA DE VENTA
# declarar variables
cliente,tubos,fierros,precio_tubo,precio_fierro="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
tubos=int(os.sys.argv[2])
fierros=int(os.sys.argv[3])
precio_tubo=float(os.sys.argv[4])
precio_fierro=float(os.sys.argv[5])

# PROCESSING
total=((tubos*precio_tubo)+(fierros*precio_fierro))

# VERIFICADOR
impuesto=(total<total)

#OUTPUT
print("#########################")
print("# Ferreteria:       EL achorado   ")
print("#########################")
print("# cliente:", cliente)
print("# tubos:", tubos,"precio:  S/.", precio_tubo)
print("# fierros:", fierros,"precio:   S/.", precio_fierro)
print("# total:   S/.", total)
print("#########################")
print("# impuesto:", impuesto)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 1000.00, ganaste la tarjeta dorada
if( total>1000):
    print("Ud ha ganado la tarjeta dorada")
# fin_if

# si el total es igual S/. 1000.00, ganaste la tarjeta de plata
if( total==1000):
    print("Ud ha ganado la tarjeta de plata")
# fin_if

# si el total es menor a S/. 1000.00, ganaste la tarjeta de cobre
if( total<1000):
    print("Ud ha ganado la tarjeta de cobre")
# fin_if
