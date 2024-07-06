from turtle import Turtle
import random


class Vehicle:
    def __init__(self):
        self.total_vehicles = []
        self.vehicles_onscreen = []
        self.__make_vehicles__()

    def __make_vehicles__(self):
        for _ in range(100):
            vehicle = Turtle(shape='square')
            vehicle.color(random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            vehicle.shapesize(stretch_len=2)
            vehicle.penup()
            vehicle.goto(1000, 1000)
            self.total_vehicles.append(vehicle)

    def pick_vehicle(self):
        vehicle = random.choice(self.total_vehicles)
        self.total_vehicles.pop(self.total_vehicles.index(vehicle))
        self.vehicles_onscreen.append(vehicle)
        vehicle.goto(random.randint(300, 400), random.randint(-250, 280))

    def vehicle_move(self):
        for vehicle in self.vehicles_onscreen:
            vehicle.fd(-10)

    def modify_vehicles(self, vehicles):
        for index in vehicles:
            vehicle = self.vehicles_onscreen.pop(index)
            vehicle.goto(1000, 1000)
            self.total_vehicles.append(vehicle)
