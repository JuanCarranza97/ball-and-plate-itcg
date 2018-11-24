while True:
    input_argv =input("Introduzca sus comandos:\n")
    
    input_argv = input_argv.split(" ")
    
    while len(input_argv) > 0:
        current = input_argv.pop(0)
        
        if current == "online":
            print("ModoOnline")
        elif current == "plot":
            print("Plot actived")
        elif current == "rerun":
            print(len(input_argv))
            if len(input_argv) >= 1:
                val = input_argv.pop(0)
                print("Se correra {} veces".format(val))
            else:
                print("Error: You should put almost 1 time")
        else:
            print("Invalid Input: {} was not specified".format(current)) 
    
    