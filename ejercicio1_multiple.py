import os

# BOLETA DE VENTA
# declarar variables
cliente,relojes,pulseras,precio_reloj,precio_pulsera="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
relojes=int(os.sys.argv[2])
pulseras=int(os.sys.argv[3])
precio_reloj=float(os.sys.argv[4])
precio_pulsera=float(os.sys.argv[5])

# PROCESSING
total=((relojes*precio_reloj)+(pulseras*precio_pulsera))

# VERIFICADOR
precio_de_venta=not(total<=pulseras)

#OUTPUT
print("#########################")
print("# Joyeria:       LA BELLEZA  ")
print("#########################")
print("# cliente:", cliente)
print("# relojes:", relojes,"precio:  S/.", precio_reloj)
print("# pulseras:", pulseras,"precio:  S/.", precio_pulsera)
print("# total:   S/.", total)
print("#########################")
print("# precio de venta:", precio_de_venta)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 300.00, ganaste una pulsera dorada
if( total>300):
    print("Ud ha ganado una pulsera dorada")
# fin_if

# si el total es igual a S/. 150.00, ganaste una pulsera de plata
if( total==150):
    print("Ud ha ganado una pulsera de plata")
#fin_if

# si el total es menor que S/. 150.00, ganaste la pulsera de cobre
if( total<150):
    print("Ud ha ganado la pulsera de cobre")
# fin_if
