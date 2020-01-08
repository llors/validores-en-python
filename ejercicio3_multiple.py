import os

# BOLETA DE VENTA
# declarar variables
cliente,baldes,tinas,precio_balde,precio_tina="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
baldes=int(os.sys.argv[2])
tinas=int(os.sys.argv[3])
precio_balde=float(os.sys.argv[4])
precio_tina=float(os.sys.argv[5])

# PROCESSING
total=((baldes*precio_balde)+(tinas*precio_tina))

# VERIFICADOR
ganancia=(total==total)

#OUTPUT
print("#########################")
print("# TIENDA :  BALTA  ")
print("#########################")
print("# cliente:", cliente)
print("# baldes:", baldes,"precio:   S/.", precio_balde)
print("# tinas:", tinas,"precio:   S/.", precio_tina)
print("total:     S/.", total)
print("#########################")
print("# ganancia:", ganancia)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 25.00, gana una tina pequeña
if( total>25):
    print("Ud ha ganado una tin pequeña")
# fin_if

# si el total es igual a S/ 25.00, no gna nada
if( total==25):
    print("ud no gna nada")
# fin_if

# si el total es menor a S/. 25.00, entonces no pondras tienda de plasticos
if(total<25):
    print("Ud no puede ganr nada")
# fin_if
