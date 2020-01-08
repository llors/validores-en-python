import os

# BOLETA DE VENTA
# declarar variables
cliente,DNI,kg_pollo,kg_res,precio_pollo,precio_res="",0,0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
DNI=int(os.sys.argv[2])
kg_pollo=int(os.sys.argv[3])
kg_res=int(os.sys.argv[4])
precio_pollo=float(os.sys.argv[5])
precio_res=float(os.sys.argv[6])

# PROCESSING
total=((kg_pollo*precio_pollo)+(kg_res*precio_res))

# VERIFICADOR
venta=(kg_res>kg_pollo)

#OUTPUT
print("#########################")
print("# CARNICERIA:   EL MANSO ")
print("#########################")
print("# cliente:", cliente)
print("# DNI:", DNI)
print("# pollo:", kg_pollo,"kg precio:  S/.", precio_pollo)
print("# res:", kg_res,"kg precio:  S/.", precio_res)
print("# total: S/.",total)
print("#########################")
print("# venta:", venta)
print("#########################")

# CONDICION MULTIPLE
# si el total supera los S/. 30.00, entonces solo comeras pollo
if( total>30):
    print("Ud solo comera pollo")
# fin_if

# si el total es igual a S/. 30.00, entonces solo comeras res
if( total==30):
    print("Ud solo comera res")
# fin_if

# si el total es menor que S/. 30.00, entonces comeras res y pollo
if( total<30):
    print("Ud comera res y pollo")
# fin_if
