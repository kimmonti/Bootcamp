import rodi #Para exportar la biblioteca de codigos de rodi
import time #Para exportar la biblioteca de tiempos

robot = rodi.RoDI()
import random

try:
    robot.move_left()
    time.sleep(1)
    while True:
        x= random.randrange(255)
        a= random.randrange(255)
        c= random.randrange(255)
        linea = robot.sense()
        print(linea[0])
        print(linea[1])
        if ((linea[0]) < 200 and (linea[1]) < 200):
            if robot.see() <= 3:
                robot.move_forward()
                robot.move(-50,-50)
                time.sleep(0.2)
                robot.move_forward()
                robot.pixel(100,0,0)
            elif robot.see() < 20 and robot.see() > 3:
                robot.move(50,50)
                robot.pixel(100,50,0)
                time.sleep(0.01)
        elif ((linea[0]) > 200 and (linea[1]) > 200):
            robot.move_stop()
            time.sleep(0.5)
            robot.move_backward()
            time.sleep(0.5)
            robot.move(-20,50)
            robot.pixel(x,a,c)
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Finalizado")
    robot.pixel(0,0,0)
    robot.move_stop()