import serial

#arduino = serial.Serial('/dev/ttyACM0',115200)

def function_1():
    print("Se metio a la funcion 1")

def function_2():
    print("Se metio a la funcion 2")

my_actions = {'CallBack':function_1,'help_string':"Esta es la cadena de ayuda 1"}
my_actions['CallBack']

#while True:
#    action = raw_input("Enter command: ")
#    
#    if action == 'help':
#        print("Pediste ayuda")
#    elif action == 'end':
#        print("Finishing ..")
#        break
#    elif action == 'On':
#        arduino.write('1')
#    elif action == 'Off':
#        arduino.write('0')
#    else:
#        print("Invalid Input")
#arduino.close()

