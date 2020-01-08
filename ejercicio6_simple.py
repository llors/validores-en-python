import os
# BOLETA DE VENTA
# Declarar variables
cliente,cajero,billeteras,p_u= "","",0,0.0

# Input
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
billeteras=int(os.sys.argv[3])
p_u=float(os.sys.argv[4])

# processing
total=(billeteras*p_u)

#Verificador
comprador_compulsivo=(total>900)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("# cliente:", cliente)
print("#item:    ",billeteras,"billeteras")
print("#p.u:      S/.", p_u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor que 900 obtiene una regalo
if (comprador_compulsivo ==True):
    print ("GANASTE UN REGALO")

#FIN_IF
