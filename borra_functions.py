import numpy as np
import math

def position_translate(position,delta):
    """
    ---Translate an specific point ---
    [x,y,z,1][1  0  0  1 = [x+dx,y+dy,z+dz,1]
              0  1  0  0
              0  0  1  0
              dx dy dz 0]
     position_translate(position,delta)
    """
    position.append(1) #Add to the enteredosition 1, we need it to multiply matrix
    pos_mat = np.matrix(position)


    translation_matrix = np.matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0],[delta[0],delta[1],delta[2],0]])

    new_pos = position*translation_matrix
    new_pos = new_pos[0,:-1]
    #new_pos = np.asarray(new_pos)
    return new_pos

def position_rotate(position,angles):
    """
    ---Rotate an specific point by the axis ---
     position_rotate(position,angles)

     position_rotate([x,y,z],[yaw,pitch,roll])

     Example:
        Rotate [0,0,1] by yaw 90 degrees

        position_rotate([0,0,1],[90,0,0])
    """
    mat_point = np.matrix(position)
    for i in range(len(angles)):
        angles[i] = math.radians(angles[i])

    rot_roll  = np.matrix([[1,0,0],[0,math.cos(angles[2]), -math.sin(angles[2])],[0,math.sin(angles[2]),math.cos(angles[2])]])
    rot_pitch = np.matrix([[math.cos(angles[1]),0,-math.sin(angles[1])],[0,1,0],[math.sin(angles[1]),0,math.cos(angles[1])]])
    rot_yaw   = np.matrix([[math.cos(angles[0]),-math.sin(angles[0]),0],[math.sin(angles[0]),math.cos(angles[0]),0],[0,0,1]])
    return mat_point*rot_roll*rot_pitch*rot_yaw

def get_servo_angle(position,links_length,base):
    if len(links_length) != 2:
        print("You should put only two links_length")
    if len(position) != 3 or len(base) != 3:
        print("This function is only available for 3 DOF with 2 links_length")

    position = position_translate(position,[-base[0],-base[1],-base[2]]).tolist()[0]
    help_link = math.sqrt(math.pow(links_length[1],2)-math.pow(position[1],2))

    costheta2 = (math.pow(position[0],2)+math.pow(position[2],2)-math.pow(links_length[0],2)-math.pow(help_link,2))/(2*links_length[0]*help_link)

    sentheta2 = [math.sqrt(1 - math.pow(costheta2,2)),-math.sqrt(1 - math.pow(costheta2,2))]
    theta2 = [math.degrees(math.atan(sentheta2[0]/costheta2)),math.degrees(math.atan(sentheta2[1]/costheta2))]

    theta1 = [math.atan(float(position[2])/float(position[0]))-math.atan((help_link*sentheta2[0])/(links_length[0]+help_link*costheta2))]
    theta1.append(math.atan(float(position[2])/float(position[0]))-math.atan((help_link*sentheta2[1])/(links_length[0]+help_link*costheta2)))
    theta1[0] = math.degrees(theta1[0])
    theta1[1] = math.degrees(theta1[1])
    return theta1
