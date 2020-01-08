import os
# BOLETA DE VENTA
# Declarar variables
cliente,cajero,carteras,p_u= "","",0,0.0

# Input
cliente=input(os.sys.argv[1])
cajero=input(os.sys.argv[2])
carteras=int(os.sys.argv[3])
p_u=float(os.sys.argv[4])

#Procesing
total= (p_u * carteras)

#Verificador
comprador_compulsivo=(total>1200)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",carteras,"carteras")
print("#p.u:      S/.", p_u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es menor que 1200 obtiene una cartera de regalo
if (comprador_compulsivo ==True):
    print ("GANASTE UNA CARTERA POR TU PREFERENCIA")
# Si el total es mayor a 1200 obtiene una tarjeta premium
if (comprador_compulsivo ==True):
    print ("GANASTE TARJETA PREMIUM")
# Si el total esta entre 1200 y 1500 gana una tarjeta de descuento
if (comprador_compulsivo ==True):
    print ("GANASTE UNA TARJETA DE DESCUENTO")

#FIN_IF
