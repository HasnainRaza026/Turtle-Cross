import time
from turtle import Screen
from player import Player
from text import Text
from vehicle import Vehicle


def vehicle_turtle_collision():
    for vehi in vehicle.vehicles_onscreen:
        if my_turtle.tur.distance(vehi) < 22:
            return True


def vehicle_crossed_screen():
    vehicles_crossed_screen = []
    for vehi in vehicle.vehicles_onscreen:
        if vehi.xcor() < -300:
            vehicles_crossed_screen.append(
                vehicle.vehicles_onscreen.index(vehi))
    return vehicles_crossed_screen


screen = Screen()
screen.title('Turtle Crossing Game')
screen.bgcolor('white')
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
text = Text()
vehicle = Vehicle()


screen.listen()
screen.onkey(my_turtle.move_up, 'w')
screen.onkey(my_turtle.move_down, 's')

vehicle_factor = 5
delay = 0.1
vehicle_counter = 0
vehicle.pick_vehicle()

while True:
    if my_turtle.tur.ycor() > 280:
        delay *= 0.6
        text.level += 1
        text.update_level()
        my_turtle.tur.goto(0, -280)
        if text.level % 5 == 0 and vehicle_factor > 2:
            vehicle_factor -= 1

    if vehicle_counter % vehicle_factor == 0:
        vehicle.pick_vehicle()
    vehicle.vehicle_move()

    if vehicle_turtle_collision():
        text.game_over()
        screen.update()
        time.sleep(2)
        break

    vehicles_crossed_screen = vehicle_crossed_screen()
    if len(vehicles_crossed_screen) != 0:
        vehicle.modify_vehicles(vehicles_crossed_screen)

    vehicle_counter += 1

    screen.update()
    time.sleep(delay)


# screen.mainloop()
