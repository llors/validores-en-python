import os

# BOLETA DE VENTA
# declarar variables
cliente,DNI,zapatillas,zapatos,precio_zapatillas,precio_zapatos="",0,0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
DNI=int(os.sys.argv[2])
zapatillas=os.sys.argv[3]
zapatos=os.sys.argv[4]
precio_zapatillas=float(os.sys.argv[5])
precio_zapatos=float(os.sys.argv[6])

# PROCESSING
total=(precio_zapatillas+precio_zapatos)

# VERIFICADOR

#OUTPUT
print("#########################")
print("# Centro de calzado:     EL ZAPATON  ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# zapatillas:", zapatillas,"precio:  S/.", precio_zapatillas)
print("# zapatos:", zapatos,"precio:  S/.", precio_zapatos)
print("# total:    S/.", total)
print("#########################")

# CONDICIONAL DOBLE
# si el total supera los S/. 300.00,le gusta los zpatazos
if( total>750):
    print("Ud le gusta los zaptasos")
else:
    print("Ud no le gusta los zapatasos")
# fin_if
