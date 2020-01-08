import os
# BOLETA DE VENTA
# Declarar variables
universidad,computadoras,p_u= "",0,0.0

# Input
universidad=os.sys.argv[1]
computadoras=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

# processing
total=(computadoras*p_u)

#Verificador
comprador_compulsivo=(total>100000)
#Output
print("#######################")
print("######Boleta de venta######")
print("#######################")
print("#item:    ",computadoras,"nro_computadoras")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera a 100 000 obtiene una tarjeta
if (comprador_compulsivo == True):
    print ("obteniste una trjeta")

#FIN_IF
