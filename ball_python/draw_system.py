import borra_functions as bf

base_points = bf.base_points(92)

loop=1
for i in base_points:
    print("El punto {} tiene coordenadas {}".format(loop,i))
    loop+=1
    
