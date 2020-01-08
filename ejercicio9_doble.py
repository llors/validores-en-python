import os
# BOLETA DE VENTA
# Declarar variables
cliente, producto, precio_u= "","",0.0

# Input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio_u=float(os.sys.argv[3])

#Procesing
total= (precio_u * producto)

#Verificador
comprador_compulsivo=( total > 100 )

#Output
print("#######################")
print("######Boleta de venta######")
print("########################")
print("# cliente:", cliente)
print("#item:    ",producto,"producto")
print("#p.u:       S/.", precio_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

#Condicion
#Cada vez que el cliente llegue a mas de 100 obtendra  30% de descuento en productos
if (comprador_compulsivo == True):
    print ("OBTUVISTE EL 30% DE DESCUENTO EN PRODUCTOS")
else:
    print ("NO GANASTE UN DESCUENTO")

#FIN_IF