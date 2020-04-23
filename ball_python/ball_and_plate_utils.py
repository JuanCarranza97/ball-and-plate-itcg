import math as _math
import json as _js
import os as _os
import numpy as _np
import matplotlib.pyplot as plt


def calculate_base_points(radio):
    points =[]
    for angle in [240,300,0,60,120,180]:
        points.append(Point([radio*_math.cos(_math.radians(angle)),radio*_math.sin(_math.radians(angle)),0]))
    return points

def plate_points(centroid_dist,scrapt_x,scrapt_y,euler_angles,translation):
    #Make the point for the translation
    point = [0,-centroid_dist,0]

    points=[]
    rot_angles = [0,-120,-240]
    for side_angle in rot_angles:
        anticlock = position_translate(point,[-(scrapt_x/2),-scrapt_y,0]).tolist()[0]
        anticlock = position_rotate(anticlock,[side_angle,0,0]).tolist()[0]
        anticlock = position_rotate(anticlock,[euler_angles[0],euler_angles[1],euler_angles[2]]).tolist()[0]
        anticlock = position_translate(anticlock,translation).tolist()[0]
        #print("anticlock = {}".format(anticlock))
        points.append(Point(anticlock))
        clock = position_translate(point,[(scrapt_x/2),-scrapt_y,0]).tolist()[0]
        clock = position_rotate(clock,[side_angle,0,0]).tolist()[0]
        clock = position_rotate(clock,[euler_angles[0],euler_angles[1],euler_angles[2]]).tolist()[0]
        clock = position_translate(clock,translation).tolist()[0]
        #print("clock = {}".format(clock))
        points.append(Point(clock))
    return points

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
    pos_mat = _np.matrix(position)


    translation_matrix = _np.matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0],[delta[0],delta[1],delta[2],0]])

    new_pos = position*translation_matrix
    new_pos = new_pos[0,:-1]
    #new_pos = _np.asarray(new_pos)
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
    mat_point = _np.matrix(position)
    for i in range(len(angles)):
        angles[i] = _math.radians(angles[i])

    rot_roll  = _np.matrix([[1,0,0],[0,_math.cos(angles[2]), -_math.sin(angles[2])],[0,_math.sin(angles[2]),_math.cos(angles[2])]])
    rot_pitch = _np.matrix([[_math.cos(angles[1]),0,-_math.sin(angles[1])],[0,1,0],[_math.sin(angles[1]),0,_math.cos(angles[1])]])
    rot_yaw   = _np.matrix([[_math.cos(angles[0]),-_math.sin(angles[0]),0],[_math.sin(angles[0]),_math.cos(angles[0]),0],[0,0,1]])
    return mat_point*rot_roll*rot_pitch*rot_yaw

def servo_angle(position_input,links_length,base_input):
    if len(links_length) != 2:
        raise Exception("You should put only two links_length")
    if isinstance(position_input,Point) and isinstance(base_input,Point):
        raise Exception("Must be an instance of %s"%Point)

    
    theta1=[]
    theta2=[]
    
    current_point=0
    side_angles = [0,120,240]
    
    for current_angle in side_angles:
        #print("--- Point {}---".format(current_point))
        #print("Angle = {}".format(current_angle))
        position = position_rotate(position_input[current_point].get_list(),[current_angle,0,0]).tolist()[0]
        base = position_rotate(base_input[current_point].get_list(),[current_angle,0,0]).tolist()[0]
        
        #print("Plate {}".format(position))
        #print("Base {}".format(base))
        #print("Before translate {}".format(position))
        position = position_translate(position,[-base[0],-base[1],-base[2]]).tolist()[0]
        #print("After translate {}".format(position))
        
        help_link = _math.sqrt(_math.pow(links_length[1],2)-_math.pow(position[1],2))

        costheta2 = (_math.pow(position[0],2)+_math.pow(position[2],2)-_math.pow(links_length[0],2)-_math.pow(help_link,2))/(2*links_length[0]*help_link)

        sentheta2 = [-_math.sqrt(1 - _math.pow(costheta2,2)),_math.sqrt(1 - _math.pow(costheta2,2))]
        
        theta2_c = []
        theta1_c = []
        
        theta2_c = [_math.degrees(_math.atan(sentheta2[0]/costheta2)),_math.degrees(_math.atan(sentheta2[1]/costheta2))]

        theta1_c = [_math.atan(float(position[2])/float(position[0]))-_math.atan((help_link*sentheta2[0])/(links_length[0]+help_link*costheta2))]
        theta1_c.append(_math.atan(float(position[2])/float(position[0]))-_math.atan((help_link*sentheta2[1])/(links_length[0]+help_link*costheta2)))
        theta1_c[0] = _math.degrees(theta1_c[0])
        theta1_c[1] = _math.degrees(theta1_c[1])
        
        if position[0] < 0:
            theta1_c[0] = theta1_c[0]+180
            theta1_c[1] = theta1_c[1]+180
        theta1.append(theta1_c)
        theta2.append(theta2_c)
        current_point+=1
        ###antipoint
        #print("--- Point {}---".format(current_point))
        #print("Angle = {}".format(current_angle))
        position = position_rotate(position_input[current_point].get_list(),[current_angle,0,0]).tolist()[0]
        base = position_rotate(base_input[current_point].get_list(),[current_angle,0,0]).tolist()[0]
        
        #print("Plate {}".format(position))
        #print("Base {}".format(base))
        #print("Before translate {}".format(position))
        position = position_translate(position,[-base[0],-base[1],-base[2]]).tolist()[0]
        #print("After translate {}".format(position))
        
        help_link = _math.sqrt(_math.pow(links_length[1],2)-_math.pow(position[1],2))

        costheta2 = (_math.pow(position[0],2)+_math.pow(position[2],2)-_math.pow(links_length[0],2)-_math.pow(help_link,2))/(2*links_length[0]*help_link)

        sentheta2 = [_math.sqrt(1 - _math.pow(costheta2,2)),-_math.sqrt(1 - _math.pow(costheta2,2))]
        
        theta2_c = []
        theta1_c = []
        
        theta2_c = [_math.degrees(_math.atan(sentheta2[0]/costheta2)),_math.degrees(_math.atan(sentheta2[1]/costheta2))]

        theta1_c = [_math.atan(float(position[2])/float(position[0]))-_math.atan((help_link*sentheta2[0])/(links_length[0]+help_link*costheta2))]
        theta1_c.append(_math.atan(float(position[2])/float(position[0]))-_math.atan((help_link*sentheta2[1])/(links_length[0]+help_link*costheta2)))
        
        theta1_c[0] = _math.degrees(theta1_c[0])
        theta1_c[1] = _math.degrees(theta1_c[1])
        
        if position[0] < 0:
            theta1_c[0] = theta1_c[0]+180
            theta1_c[1] = theta1_c[1]+180
        theta1.append(theta1_c)
        theta2.append(theta2_c)
        current_point+=1
        
    return theta1,theta2

def draw_axis(axis_x,axis_y,axis_z,ax,fig):
    ax.set_xlim(-axis_x,axis_x)
    ax.set_ylim(-axis_y,axis_y)
    ax.set_zlim(0,axis_z)
    x = [-axis_x,0]
    y = [0,0]
    z = [0,0]
    ax.plot3D(x,y,z,'--r')
    #fig.canvas.draw()
    x = [0,axis_x]
    y = [0,0]
    z = [0,0]
    ax.plot3D(x,y,z,'r')
    #fig.canvas.draw()
    x = [0,0]
    y = [-axis_y,0]
    z = [0,0]
    ax.plot3D(x,y,z,'--b')
    #fig.canvas.draw()
    x = [0,0]
    y = [0,axis_y]
    z = [0,0]
    ax.plot3D(x,y,z,'b')
    #fig.canvas.draw()
    x = [0,0]
    y = [0,0]
    z = [0,axis_z]
    ax.plot3D(x,y,z,'g')
    #fig.canvas.draw()

def draw_by_points(points,ax,fig,color):
    x,y,z = points_to_xyz(points)
    
    x.append(x[0])
    y.append(y[0])
    z.append(z[0])
    
    ax.plot3D(x,y,z,c=color)
    #fig.canvas.draw()

def points_to_xyz(points):
    x = []
    y = []
    z = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
        z.append(point.z)
    return x,y,z

def draw_servo(base_points,plate_points,servos_length,angles,ax,fig):
    servo_points=[]
    rot_angle = [0,120,240]
    
    point = 0
    
    for side_angle in rot_angle:
        end_servo = []
        #print("Point {}".format(point))
        rotated_point = position_rotate(base_points[point].get_list(),[side_angle,0,0]).tolist()[0] 
        #print("Grado 1 = {}\nGrado 2 = {}".format(angles[point][0],angles[point][1]))
        #La solucion es con theta1[1]
        end_servo.append([rotated_point[0]+servos_length*_math.cos(_math.radians(angles[point][0])),rotated_point[1],rotated_point[2]+servos_length*_math.sin(_math.radians(angles[point][0]))])
        end_servo.append([rotated_point[0]+servos_length*_math.cos(_math.radians(angles[point][1])),rotated_point[1],rotated_point[2]+servos_length*_math.sin(_math.radians(angles[point][1]))])
        end_servo[0] = position_rotate(end_servo[0],[-side_angle,0,0,]).tolist()[0]
        end_servo[1] = position_rotate(end_servo[1],[-side_angle,0,0,]).tolist()[0]
        servo_points.append(end_servo)
        #print("The length 1 is {}".format(two_points_length(servo_points[point][0],base_points[point])))
        #print("The length 2 is {}".format(two_points_length(servo_points[point][1],base_points[point])))
        
        point+=1
        end_servo = []
        #print("Point {}".format(point))
        rotated_point = position_rotate(base_points[point].get_list(),[side_angle,0,0]).tolist()[0] 
        #print("Grado 1 = {}\nGrado 2 = {}".format(angles[point][0],angles[point][1]))
        ###La solucion es con theta1[0] (Se invierte la posision)
        end_servo.append([rotated_point[0]+servos_length*_math.cos(_math.radians(angles[point][0])),rotated_point[1],rotated_point[2]+servos_length*_math.sin(_math.radians(angles[point][0]))])
        end_servo.append([rotated_point[0]+servos_length*_math.cos(_math.radians(angles[point][1])),rotated_point[1],rotated_point[2]+servos_length*_math.sin(_math.radians(angles[point][1]))])
        end_servo[0] = position_rotate(end_servo[0],[-side_angle,0,0,]).tolist()[0]
        end_servo[1] = position_rotate(end_servo[1],[-side_angle,0,0,]).tolist()[0]
        servo_points.append(end_servo)
        #print("The length 1 is {}".format(two_points_length(servo_points[point][0],base_points[point])))
        #print("The length 2 is {}".format(two_points_length(servo_points[point][1],base_points[point])))
        point+=1
    

    for i in range(6):
        ax.plot3D([base_points[i].x,servo_points[i][0][0]],[base_points[i].y,servo_points[i][0][1]],[base_points[i].z,servo_points[i][0][2]],'k')
        ax.plot3D([plate_points[i].x,servo_points[i][0][0]],[plate_points[i].y,servo_points[i][0][1]],[plate_points[i].z,servo_points[i][0][2]],'k')
        #fig.canvas.draw()
        ax.plot3D([base_points[i].x,servo_points[i][1][0]],[base_points[i].y,servo_points[i][1][1]],[base_points[i].z,servo_points[i][1][2]],':k')
        ax.plot3D([plate_points[i].x,servo_points[i][1][0]],[plate_points[i].y,servo_points[i][1][1]],[plate_points[i].z,servo_points[i][1][2]],':k')
        #fig.canvas.draw()

class Point:
    def __init__(self,cordinates):
        if isinstance(cordinates,list):
            if len(cordinates) == 3:
                self.x = cordinates[0]
                self.y = cordinates[1]
                self.z = cordinates[2]
            else:
                raise Exception("Must have 3 items")
        else:
            raise Exception("Must be a List")
    
    def get_list(self):
        return [self.x,self.y,self.z]
    def __str__(self):
        return "Point(x=%d, y=%d, z=%d)\n"%(self.x,self.y,self.z)
    
    def __repr__(self):
        return str(self)

class Platform_config:
    def __init__(self,json_path,plot=False):
        self.json_path = json_path
        self.read_keys()
        self.init_variables()
        self.base_points = calculate_base_points(self.base_length)
        self.plot = plot
        if plot:
            plt.ion()
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111,projection='3d')
            self.draw_axis()
            self.set_platform(self.home_angles,self.home_translation)

    def read_keys(self):
        """
        jvutjguj
        """
        if _os.path.exists(self.json_path):
            json_file = open(self.json_path)
            platform_json = _js.load(fp=json_file)
            self.platform_dic = dict(platform_json["Platform"])
            self.servos_dic = dict(platform_json["Servos"])
        else: 
            raise Exception("Path Not Valid")
        
    def init_variables(self):
        
        self.base_length = self.platform_dic["base_length"]
        self.servo_links = self.platform_dic["servo_links"]
        self.scrapt_x = self.platform_dic["scrapt_x"]
        self.scrapt_y = self.platform_dic["scrapt_y"]
        self.centroid_dist = self.platform_dic["centroid_dist"]
        self.axis_x = self.platform_dic["axis"]["x"]
        self.axis_y = self.platform_dic["axis"]["y"]
        self.axis_z = self.platform_dic["axis"]["z"]
        home_translation = self.platform_dic["home"]["translation"]
        home_angles = self.platform_dic["home"]["angles"]
        self.home_translation = [
            home_translation["x"],
            home_translation["y"],
            home_translation["z"]
        ]
        self.home_angles = [
            home_angles["yaw"],
            home_angles["pitch"],
            home_angles["roll"]
        ]
        self.min_servo_signal = self.servos_dic["min_servo_signal"]
        self.max_servo_signal = self.servos_dic["max_servo_signal"]
        self.min_signal_degree = self.servos_dic["min_signal_degree"]
        self.max_signal_degree = self.servos_dic["max_signal_degree"]
        self.pca_channels = self.servos_dic["pca_channels"]

    
    def update_plate_points(self,angle,translation):
        self.plate_points = plate_points(self.centroid_dist,self.scrapt_x,self.scrapt_y,angle,translation)
    
    def update_servo_angle(self,angle,translation):
        self.update_plate_points(angle,translation)
        try:
            self.servo_angles_1,self.servo_angles_2 = servo_angle(self.plate_points,self.servo_links,self.base_points)
            return True
        except ValueError:
            print("It's not possible to set current position on this plataform")
            return False

    def draw_axis(self):
        plt.cla()
        draw_axis(self.axis_x,self.axis_y,self.axis_z,self.ax,self.fig)
    
    def set_platform(self,angle,translation):
        rc = self.update_servo_angle(angle,translation)
        if self.plot and rc: 
            self.draw_axis()
            draw_by_points(self.base_points,self.ax,self.fig,'orangered')
            draw_by_points(self.plate_points,self.ax,self.fig,'dodgerblue')

            draw_servo(self.base_points,self.plate_points,self.servo_links[0],self.servo_angles_1,self.ax,self.fig)
            self.fig.canvas.draw()
