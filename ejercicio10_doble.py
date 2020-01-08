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
comprador_compulsivo=( total > 120 )

#Output
print("#######################")
print("####Boleta de venta####")
print("#######################")
print("# cliente:", cliente)
print("#item:    ",juguetes," juguetes")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera 120 gana un PREMIO
if (comprador_compulsivo == True):
    print ("GANASTE UN PREMIO")
else:
    print ("NO GANASTE UN PREMIO")
#FIN_IF