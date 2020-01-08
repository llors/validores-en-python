import os
# BOLETA DE VENTA
# Declarar variables
cliente,nro_cajas,precio_caja= "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_cajas=int(os.sys.argv[2])
precio_caja=float(os.sys.argv[3])

#Procesing
total= (precio_caja * nro_cajas)

#Verificador
comprador_compulsivo=( total > 50 )

#Output
print("#######################")
print("######Boleta de venta######")
print("#######################")
print("# comprador:", cliente)
print("#item:    ",nro_cajas,"nro_cajas")
print("#precio_caja:       S/.", precio_caja)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 50 ganas un premio
if (comprador_compulsivo ==True):
    print ("GANAS UN PREMIO")
# Si el total es menor que 50 accede aL PREMIO
if (comprador_compulsivo ==True):
    print ("ACCEDISTE AL PREMIO")
# Si el total esta entre
if (comprador_compulsivo ==True):
    print ("")

#FIN_IF
