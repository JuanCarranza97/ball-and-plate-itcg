import borra_functions as bf

base_points = bf.base_points(92)
plate_points = bf.plate_points(72.9,6,[0,0,0],[0,0,110])

plate_point  = plate_points[0]
base_point = base_points[0]

new_plate = bf.position_translate(plate_point,[-base_point[0],-base_point[1],-base_point[2]]).tolist()[0]

theta1,theta2 = bf.get_servo_angle(new_plate,[58.31,61.64],[0,0,0])

print("Base point = {}".format(base_point))
print("Plate point = {}".format(plate_point))
print("Links length = {}".format([58.31,61.64]))
print("Theta 1 = {}".format(theta1))
print("Theta 2 = {}".format(theta2))
