import os
# BOLETA DE VENTA
# Declarar variables
comprador,cajas,precio_caja= "",0,0.0

# Input
comprador=os.sys.argv[1]
cajas =int(os.sys.argv[2])
precio_caja =float(os.sys.argv[3])

# processing
total=(cajas*precio_caja)

#Verificador
comprador_compulsivo=( total > 450 )

#Output

print("#######################")
print("######Boleta de venta######")
print("########################")
print("# comprador:", comprador)
print("#item:    ",cajas,"nro_cajas")
print("#precio_caja:       S/.", precio_caja)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 450 accede a ganar un premio
if (comprador_compulsivo ==True):
    print ("ACCEDISTE  GANAR UN PREMIO")

#FIN_IF