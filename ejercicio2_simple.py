# ejercicio 2
import os
# BOLETA DE VENTA
# Declarar variables
cliente, producto, p_u= "","",0.0

# Input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
p_u=float(os.sys.argv[3])

#Verificador
comprador_compulsivo=( p_u > 100 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#####################")
print("# cliente:", cliente)
print("#item:    ",producto,"producto")
print("#p.u:       S/.", p_u)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

#Cada vez que el cliente llegue a mas de 100 obtendra un vale de 30% de descuento en productos
if (comprador_compulsivo == True):
    print ("FELICIDADES OBTUVISTE EL 30% DE DESCUENTO EN PRODUCTOS")

#FIN_IF

