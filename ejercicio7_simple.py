import os
# BOLETA DE VENTA
# Declarar variables
cliente,gaseosas,precio_unitario= "",0,0.0

# Input
cliente=os.sys.argv[1]
gaseosas=int(os.sys.argv[2])
precio_unitario=float(os.sys.argv[3])

# processing
total=(gaseosas*precio_unitario)

#Verificador
comprador_compulsivo=( total > 200 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#######################")
print("# cliente:", cliente)
print("#item:    ",gaseosas,"gaseosas")
print("#precio unitario:       S/.", precio_unitario)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el monto en menor que 200 obtiene un paneton
if (comprador_compulsivo ==True):
    print ("GANSTE UN PANETON")

#FIN_IF
