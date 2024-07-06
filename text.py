from turtle import Turtle


class Text:
    def __init__(self):
        self.level = 1
        self.level_instance = Turtle()
        self.level_instance.speed(0)
        self.level_instance.penup()
        self.level_instance.hideturtle()
        self.level_instance.goto(-220, 250)

        self.gameover_instance = Turtle()
        self.gameover_instance.speed(0)
        self.gameover_instance.penup()
        self.gameover_instance.hideturtle()
        self.gameover_instance.goto(0, 0)

        self.update_level()

    def update_level(self):
        self.level_instance.clear()
        self.level_instance.write(
            f"Level: {self.level}", align="center", font=('Courier', 20, 'bold'))

    def game_over(self):  # <---------- Not working, idk why
        self.gameover_instance.clear()
        self.gameover_instance.write(
            "Game Over", align="center", font=('Courier', 30, 'bold'))
