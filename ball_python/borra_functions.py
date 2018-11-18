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
    position.pop()
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

def base_points(radio):
    points =[]
    for angle in [240,300,0,60,120,180]:
        points.append([radio*math.cos(math.radians(angle)),radio*math.sin(math.radians(angle)),0])
    return points

def plate_points(centroid_dist,scrap,euler_angles,translation):
    #Make the point for the translation
    point = [0,-centroid_dist,0]

    points=[]
    rot_angles = [0,-120,-240]

    for side_angle in rot_angles:
        anticlock = position_translate(point,[-(scrap/2),-scrap,0]).tolist()[0]
        anticlock = position_rotate(anticlock,[euler_angles[0]+side_angle,euler_angles[1],euler_angles[2]]).tolist()[0]
        anticlock = position_translate(anticlock,translation).tolist()[0]
        #print("anticlock = {}".format(anticlock))
        points.append(anticlock)
        clock = position_translate(point,[(scrap/2),-scrap,0]).tolist()[0]
        clock = position_rotate(clock,[euler_angles[0]+side_angle,euler_angles[1],euler_angles[2]]).tolist()[0]
        clock = position_translate(clock,translation).tolist()[0]
        #print("clock = {}".format(clock))
        points.append(clock)
    return points

def points_to_xyz(points):
    x = []
    y = []
    z = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x,y,z

def draw_by_points(points,ax,fig,color):
    x,y,z = points_to_xyz(points)
    
    x.append(x[0])
    y.append(y[0])
    z.append(z[0])
    
    ax.plot3D(x,y,z,c=color)
    fig.canvas.draw()
    
def draw_axis(axis_x,axis_y,axis_z,ax,fig):
    ax.set_xlim(-axis_x,axis_x)
    ax.set_ylim(-axis_y,axis_y)
    ax.set_zlim(0,axis_z)

    x = [-axis_x,0]
    y = [0,0]
    z = [0,0]
    ax.plot3D(x,y,z,'--r')
    fig.canvas.draw()
    x = [0,axis_x]
    y = [0,0]
    z = [0,0]
    ax.plot3D(x,y,z,'r')
    fig.canvas.draw()
    x = [0,0]
    y = [-axis_y,0]
    z = [0,0]
    ax.plot3D(x,y,z,'--b')
    fig.canvas.draw()
    x = [0,0]
    y = [0,axis_y]
    z = [0,0]
    ax.plot3D(x,y,z,'b')
    fig.canvas.draw()
    x = [0,0]
    y = [0,0]
    z = [0,axis_z]
    ax.plot3D(x,y,z,'g')
    fig.canvas.draw()
    
