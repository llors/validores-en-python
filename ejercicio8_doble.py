import os
# BOLETA DE VENTA
# Declarar variables
cliente,kg,p_unidad ="",0,0.0

# Input
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
p_unidad=float(os.sys.argv[3])

#Procesing
total= (p_unidad * kg)

#Verificador
comprador_compulsivo=(total>10)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", p_unidad)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 10 el vendedor esta feliz
if (comprador_compulsivo == True):
    print ("el vendedor esta feliz")
else:
    print ("el vendedor no esta feliz ")

#FIN_IF
