import os

# BOLETA DE VENTA
# declarar variables
cliente,cuaderno,libro,p_cuaderno,p_libro="",0,0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
cuaderno=os.sys.argv[2]
libro=os.sys.argv[3]
p_cuaderno=float(os.sys.argv[4])
p_libro=float(os.sys.argv[5])

#PROCESSING
total_a_pagar=((cuaderno*p_cuaderno)+(libro*p_libro))

#vVERIFICADOR
total_a_gastar=(not(total_a_pagar<80))

#OUTPUT
print("###########################")
print("#  Librería:     el poeta")
print("###########################")
print("# cliente:", cliente)
print("# cuaderno01:", cuaderno,"# precio:  S/.", p_cuaderno)
print("# cuaderno02:", libro,"# precio:  S/.", p_libro)
print("# total:  S/.", total_a_pagar)
print("###########################")
print("# total a gastar:", total_a_gastar)
print("###########################")

# CONDICIONAL SIMPLE
# si el total a pagar no supera los S/. 50.00, no podras ir a clases
if( total_a_pagar<50):
    print("Ud no podra asistir a clases")
# fin_if
