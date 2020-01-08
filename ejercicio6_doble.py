import os

# BOLETA DE VENTA
# Declarar variables
cliente,nro_manzanas,p_u = "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_manzanas=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * nro_manzanas)

#Verificador
comprador_compulsivo=( total > 50 )

#Output

print("#######################")
print("######Boleta de venta######")
print("# cliente:", cliente)
print("#item:    ",nro_manzanas,"nro_manzanas")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor que 50 entonces estas bien nutrido
if ( comprador_compulsivo ==True):
    print ("estas bien nutrido")
else:
    print ("no estas nutrido")
#FIN_IF
