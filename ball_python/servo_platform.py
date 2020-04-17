class servos_serial:
    from serial.tools.list_ports import comports as _comports
    from serial import Serial 

    def __init__(self,port,baud_rate=115200):
        self.port = self.get_serial_port(port)
        self.arduino = self.Serial(self.port.device,baud_rate) 
            
    def get_serial_port(self,port):
        for comport in self._comports():
            if comport.name == port or comport.device == port:
                return comport 
        raise Exception("Entered serial port %s is not in available ports."%port)
             
    
    
