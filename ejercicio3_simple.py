import os
# BOLETA DE VENTA
# Declarar variables
cliente,kg,Precio_u ="",0,0.0

# Input
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
Precio_u=float(os.sys.argv[3])

# processing
total=(kg*Precio_u)

#Verificador
comprador_compulsivo=(total>100)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", Precio_u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 100 obtendran un premio
if (comprador_compulsivo ==True):
    print ("OBTUVISTE UN PREMIO")
#FIN_IF
