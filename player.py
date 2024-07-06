from turtle import Turtle

class Player:
    def __init__(self):
        self.tur = Turtle(shape='turtle')
        self.tur.speed(0)
        self.tur.penup()
        self.tur.setheading(90)
        self.tur.goto(0, -280)


    def move_up(self):
        self.tur.fd(20)

    def move_down(self):
        self.tur.fd(-20)
