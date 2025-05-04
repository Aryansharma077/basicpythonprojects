command=""
carstarted=False
while True:
    command= input("> ").lower()
    if command== "start":
        if carstarted==False:
            print("car started")
            carstarted = True
        else:
            print("car has already started")
    elif command== "stop":
        if carstarted:
            print("car stopped")
            carstarted = False
        else:
            print("car has already stopped")
    elif command=="help":
        print('''
start- to start the car
stop- to stop the car
exit - to exit''')
    elif command=="exit":
        break
    else:
            print("i dont understand")
