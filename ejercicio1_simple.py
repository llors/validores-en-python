# ejercicio 1
import os
# BOLETA DE VENTA
# Declarar variables
clienton,cervezas, p_u="", 0, 0.0

# Input
clienton=os.sys.argv[1]
cervezas=int(os.sys.argv[2])
p_u= float(os.sys.argv[3])

# processing
total=(cervezas*p_u)

#Verificador
comrador_compulsivo=(total > 100)

#Output
print("#######################")
print("######Boleta de venta######")
print("######################")
print("# cliente:", clienton)
print("#item:    ",cervezas,"nro cervesas")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comrador_compulsivo)

#si el total es mayor que 100 entonces tiene un bono de descuento.
if (comrador_compulsivo ==True):
    print ("Ganaste un bono de descuento en tu proxima compra")

#FIN_IF
