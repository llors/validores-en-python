import os
# BOLETA DE VENTA
# declarar variables
cliente,avion,dron,precio_avion,precio_dron="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
avion=os.sys.argv[2]
dron=os.sys.argv[3]
precio_avion=float(os.sys.argv[4])
precio_dron=float(os.sys.argv[5])

# PROCESSING
total=(precio_avion+precio_dron)

# VERIFICADOR
IGV=(total>=10 or 10>=total)

#OUTPUT
print("#########################")
print("# VOLETA DE VENTA ")
print("#########################")
print("# cliente:", cliente)
print("# avion01:", avion," precio:  S/.", precio_avion)
print("# avion03:", dron," precio:  S/.", precio_dron)
print("# total:   S/.", total)
print("#########################")
print("# IGV:", IGV)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera a S/. 10 000 000.00, usted viajara donde quiera
if( total>10000000):
    print("Ud viaja donde quiera")
else:
    print("Ud no viajara donde quiera")
# fin_if
