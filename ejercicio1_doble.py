# ejercicio 1 doble
import os

# BOLETA DE VENTA
# declarar variables
cliente,manzana,freza,naranja,precio_manzana,precio_freza,precio_naranja="",0,0,0,0.0,0.0,0.0
# INPUT
cliente=os.sys.argv[1]
manzana=int(os.sys.argv[2])
freza=int(os.sys.argv[3])
naranja=int(os.sys.argv[4])
precio_manzana=float(os.sys.argv[5])
precio_freza=float(os.sys.argv[6])
precio_naranja=float(os.sys.argv[7])

# PROCESSING
total=((manzana*precio_manzana)+(freza*precio_freza)+(naranja*precio_naranja))

# VERIFICADOR
cantidad_frutas=not(total!=manzana or total==total)

#OUTPUT
print("#########################")
print("# Centro comercial:     BANCES  ")
print("#########################")
print("# cliente:", cliente)
print("# manzana:", manzana,"precio:   S/.", precio_manzana)
print("# frzas:", freza,"precio:   S/.", precio_freza)
print("# naranjas:", naranja,"precio:   S/.", precio_naranja)
print("# total:   S/.", total)
print("#########################")
print("# cantidad de frutas:", cantidad_frutas)
print("#########################")

# CONDICIONAL DOBLE
# si el total de frutas es mayor a S/. 130.00, entonces abra jugo para toda la familia
if( total>130):
    print("jugo para toda la familia")
else:
    print("el jugo no alcanza para la familia")
# fin_if
