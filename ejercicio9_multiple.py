import os
# BOLETA DE VENTA
# Declarar variables
comprador,granadillas,p_u = "",0,0.0

# Input
comprador=os.sys.argv[1]
granadillas=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * granadillas)

#Verificador
comprador_compulsivo=( total > 70 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", comprador)
print("#item:    ",granadillas,"granadillas")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor que 70 entonces gana una rifa
if (comprador_compulsivo ==True):
    print ("GANASTE UNA RIFA")
# Si el total es menor que 70 gana una docena de granadillas
if (comprador_compulsivo ==True):
    print ("GANASTE UNA DOCENA DE GRANADILAS")
# Si el total esta entre 54 y 65 gana un descuento en la sgnte compra
if (comprador_compulsivo ==True):
    print ("GANASTE UN DESCUENTO EN SU PROXIMA COMPRA")

#FIN_IF
