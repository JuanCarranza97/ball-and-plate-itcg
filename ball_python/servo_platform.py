from platform import system as _system
from serial.tools.list_ports import comports as _comports
from serial import Serial as _serial
import re as _re
import argparse as _argparse
from time import sleep as _sleep

class servos_serial:
    def __init__(self,port,baud_rate=115200):
        self.port = self._get_serial_port(port)
        self.arduino = _serial(self.port.device,baud_rate) 
            
    def _get_serial_port(self,port):
        if _system() == "Windows":
            port = port.upper()
        available_ports = []
        for comport in _comports():
            available_ports.append(comport.device)
            if comport.name == port or comport.device == port:
                return comport 
        raise Exception("Entered serial port {} is not in available ports. Available:{}".format(port,available_ports))
    
    def set_platform(self,angles):
        if isinstance(angles,list):
            if len(angles) == 6:
                self.send_data("p",angles)
            else:
                raise Exception("Len of entered list ({}) is not 6".format(angles))
        else:
            raise("Entered argument angles is not list")


    def set_servo(self,servo,angle):
        """
            Set specific servo to specific position
        """
        servo = int(servo)
        angle = int(angle)
        self.send_data("s",[servo,angle])

    def _list_to_str(self,values):
        if not isinstance(values,list):
            values = [values]
        values = [int(i) for i in values] 
        text_to_send = ""
        for index,val in enumerate(values):
            if index == 0:
                text_to_send += "%d"%val
            else:
                text_to_send += ",%d"%val
        return text_to_send

    def send_data(self,character,values):
        """
            This method is used to send data from python to arduino board

            character: ONE character
               values: List of int values to send
        """
        text_to_send = str(character)+self._list_to_str(values)
        matcher = _re.compile(r'[A-Za-z][-]?[0-9]+([,][-]?[0-9]+)*$')
        if matcher.match(text_to_send):
            self.arduino.write(str.encode("%s\n"%text_to_send))
        else:
            raise Exception("Entered text to send is not valid. TextToSend=%s"%text_to_send)

    def close_port(self):
        self.arduino.close()
        

if __name__ == "__main__":
    parser = _argparse.ArgumentParser(description='Python module to send servo positions to any platform')

    parser.add_argument('--port', dest='port', 
                        type=str,required = True,
                        help='COM port to connect')

    parser.add_argument('--servo', dest='servo', 
                        type=int,help='Servo to set position')

    parser.add_argument('--angle', dest='angle', 
                        type=int,help='Servo angle')

    parser.add_argument('--platform', dest='platform', 
                        type=str,help='Set platform angles')
    
    args = parser.parse_args()    

    arduino = servos_serial(args.port)
    print("Python serial demo for PCA9685 and arduino :)\n")
    _sleep(2)
    print("Turning ON LED ")
    arduino.send_data("l",1)
    _sleep(.5)
    print("Turning OFF LED ")
    arduino.send_data("l",0)
    _sleep(.5)
    try:
        if args.platform:
            values = args.platform.split(",")
            print("Writing values to platform ... {}".format(values))
            arduino.set_platform(values)
        else:
            print("Setting servo %d to %d grades"%(args.servo,args.angle))
            arduino.set_servo(args.servo,args.angle)
    finally:
        print("\n\nClosing port... :)")
        arduino.close_port()

    
    

    