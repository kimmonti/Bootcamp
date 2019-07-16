'''try: #Intentar algo
    while True:
        x= random.randrange(255)
        a= random.randrange(255)
        c= random.randrange(255)
        linea = robot.sense()
        if robot.see() < 10 and robot.see() >= 0:
            if (linea[0]) < 80 and (linea[1]) < 80:
            robot.move.forward()
            robot.move(-50,-50)
            time.sleep(0.2)
            robot.move_forward()
            robot.pixel(100,0,0)
        elif (linea[0]) > 80 and (linea[1]) < 80:
            robot.pixel(x,a,c)
            time.sleep(0.01)
            robot.move(-50,-50)
            robot.move_left(-20,50)
except KeyboardInterrupt: #excepto cuando hay una interrupcion por teclado
    print("Finalizado")
    robot.pixel(0,0,0)
    robot.move_stop()'''