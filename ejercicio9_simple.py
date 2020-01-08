import os

# BOLETA DE VENTA
# declarar variables
cliente,celular1,celular2,precio_celular1,precio_celular2="","","",0.0,0.0

# INPUT
cliente=os.sys.argv[1]
celular1=os.sys.argv[2]
celular2=os.sys.argv[3]
precio_celular1=float(os.sys.argv[4])
precio_celular2=float(os.sys.argv[5])

# PROCESSING
total=(precio_celular1+precio_celular2)

# VERIFICADOR
ganancia=(total==total and total!=total)

#OUTPUT
print("#########################")
print("# Centro comercial:    lo mejor de marcas ")
print("#########################")
print("# cliente:", cliente)
print("# celular:", celular1," precio:  S/.", precio_celular1)
print("# celular:", celular2," precio:  S/.", precio_celular2)
print("# total:  S/.", total)
print("#########################")
print("# ganancia:", ganancia)
print("#########################")

# CONDICIONAL DOBLE
# si el total no supera los S/. 200.00, habra conprado celulares en la cachina
if( total<200):
    print("Ud a comprado celulares en la cachina")
# fin_if
