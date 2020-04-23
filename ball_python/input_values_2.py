import argparse as _argparse
import borra_function_2 as bf

status = "offline" 
plot = False

#---------------------------------------------------------------------------------------------------------       

#---------------------------------------------------------------------------------------------------------
def main():
    parser = _argparse.ArgumentParser(description='Python module to move the platform with arduino or raspberry')

    #parser.add_argument('--port', dest='port', 
    #                    type=str,required = True,
    #                    help='COM port to connect')
#
    #parser.add_argument('--servo', dest='servo', 
    #                    type=int,help='Servo to set position')
#
    #parser.add_argument('--angle', dest='angle', 
    #                    type=int,help='Servo angle')
#
    #parser.add_argument('--platform', dest='platform', 
    #                    type=str,help='Set platform angles')
    
    parser.add_argument('--connection', dest='connection', 
                        type=str.lower,help='Select if you going to use Arduino or Raspberry',
                        choices=("raspberry","arduino"))
    args = parser.parse_args()    

    print ("Coonnection is %s"%args.connection)
    #arduino = servos_serial(args.port)
    #print("Python serial demo for PCA9685 and arduino :)\n")
    #_sleep(2)
    #print("Turning ON LED ")
    #arduino.send_data("l",1)
    #_sleep(.5)
    #print("Turning OFF LED ")
    #arduino.send_data("l",0)
    #_sleep(.5)
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    exit(main())