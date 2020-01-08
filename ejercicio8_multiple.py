import os
# BOLETA DE VENTA
# Declarar variables
cliente,juguetes,p_u= "",0,0.0

# Input
cliente=os.sys.argv[1]
juguetes=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * juguetes)

#Verificador
comprador_compulsivo=( total > 100 )

#Output
print("#######################")
print("####Boleta de venta####")
print("########")
print("# cliente:", cliente)
print("#item:    ",juguetes,"nro_juguetes")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera 100 gana un pase para el cine
if (comprador_compulsivo == True):
    print ("GANASTE UN PASE AL CINE")
# Si el total es menor que 100 gana un premio sorpresa
if (comprador_compulsivo == True):
    print ("GANASTE UN PREMIO SORPRESA")
# Si el total no llega a ser mayor que 100 tiene un vale de descuento
if (comprador_compulsivo == True):
    print ("VALE DE DESCUENTO")

#FIN_IF
