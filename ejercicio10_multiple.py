import os
# BOLETA DE VENTA
# Declarar variables
cliente, cervezas, p_u= "", 0, 0.0

# Input
cliente = os.sys.argv[1]
cervezas =int(os.sys.argv[2])
p_u= float(os.sys.argv[3])

#Procesing
total= (p_u * cervezas)

#Verificador
comrador_compulsivo=(total > 80)

#Output
print("#######################")
print("######Boleta de venta######")
print("#######################")
print("# cliente:", cliente)
print("#item:    ",cervezas,"nro cervesas")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comrador_compulsivo)

#si el total es menor que 80 entonces tiene un bono
if (comrador_compulsivo == True):
    print ("GANASTE UN BONO ")
# Si el total es mayor que 150 entonces obtiene una entrada al cine
if (comrador_compulsivo ==True):
    print ("GANASTE UNA ENTRADA AL CINE ")
# Si el total esta entre 80 y 100 entonces obtiene 2 cervezas mas
if (comrador_compulsivo ==True):
    print ("GANASTE 2 CERVEZAS")

#FIN_IF
