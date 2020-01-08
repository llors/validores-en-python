import os
# BOLETA DE VENTA
# Declarar variables
cliente,gaseosas,pu= "",0,0.0

# Input
cliente=os.sys.argv[1]
gaseosas=os.sys.argv[2]
pu=float(os.sys.argv[3])

#Procesing
total= (pu * gaseosas)

#Verificador
comprador_compulsivo=( total > 300 )

#Output
print("#######################")
print("######Boleta de venta######")
print("# cliente:", cliente)
print("#item:    ",gaseosas,"gaseosas")
print("#precio unitario:       S/.", pu)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el monto en menor que 300 obtiene un premio
if (comprador_compulsivo ==True):
    print ("GANSTE UN PREMIO")
   # Si el total si esta entre 400 y 500 gana un vale de compra
if (comprador_compulsivo ==True):
    print ("GANASTE UN VALE DE COMPRA")
#FIN_IF
