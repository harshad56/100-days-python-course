from turtle import Turtle


class Alien(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('circle')
        self.color(color)
        self.penup()
        self.goto(position)
        self.x_move = 0.5
        self.y_move = 0
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reverse(self):
        self.x_move *= -1


class Ground(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=3)
        self.goto(x, y)


class Cannon(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        #self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


class Shield(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.goto(x, -300)


class Missile(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.goto(position)
        self.x_move = 0
        self.y_move = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


class Bomb(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(position)
        self.x_move = 0
        self.y_move = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-150, 330)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color('white')
        self.penup()
        self.goto(150, 330)
        self.hideturtle()
        self.update_lives()

    def update_lives(self):
        self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.update_lives()


from turtle import Screen
from components import Cannon, Ground, Alien, Missile, Bomb, Shield
from scoreboard import Scoreboard, Lives
import random as r

screen = Screen()
screen.setup(width=800, height=1000)
screen.bgcolor('black')
screen.title('Space Invaders')
screen.tracer(0)
# tracer set to 0 means that components are drawn on screen without delay
# components not on screen until game_is_on & screen.update() takes effect


# game components
def create_missile():
    position = (cannon.xcor(), cannon.ycor())
    missile = Missile(position)
    missiles.append(missile)


def create_bomb(x):
    position = (x.xcor(), x.ycor())
    bomb = Bomb(position)
    bombs.append(bomb)


def create_aliens():
    alien_type = [('blue', 300), ('red', 260), ('yellow', 220), ('orange', 180)]
    for t in alien_type:
        for x in range(-250, 250, 50):
            alien = Alien((x, t[1]), t[0])
            aliens.append(alien)


def create_shields():
    positions = [-140, -130, -120, -110, 110, 120, 130, 140]
    for position in positions:
        shield = Shield(position)
        shields.append(shield)


scoreboard = Scoreboard()
lives = Lives()
cannon = Cannon((0, -350))
shields = []
create_shields()
earth = [Ground(x, -360) for x in range(-400, 400, 60)]
aliens = []
create_aliens()
missiles = []
bombs = []


screen.listen()
screen.onkey(cannon.go_right, 'Right')
screen.onkey(cannon.go_left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    for alien in aliens:
        alien.move()

    # aliens moving down
    for alien in aliens:
        if alien.xcor() > 350 or alien.xcor() < -350:
            alien.goto(alien.xcor(), alien.ycor()-20)
            alien.reverse()

    # missile
    screen.onkey(create_missile, 'space')
    for missile in missiles:
        missile.move()
        for alien in aliens:
            if alien.distance(missile) < 20:
                alien.hideturtle()
                aliens.remove(alien)
                missile.hideturtle()
                missiles.remove(missile)
                scoreboard.increase_score()

    # bombs
    random_num = r.randint(1, 150)
    if random_num == 1:
        random_alien = r.choice(aliens)
        create_bomb(random_alien)
    for b in bombs:
        b.move()
        if b.distance(cannon) < 10:
            bombs.remove(b)
            b.hideturtle()
            lives.decrease_lives()
        elif b.ycor() < -360:
            b.hideturtle()
            bombs.remove(b)
        for s in shields:
            if s.distance(b) < 10:
                s.hideturtle()
                shields.remove(s)
                b.hideturtle()
                bombs.remove(b)

    if lives.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    if not aliens:
        create_aliens()

screen.exitonclick()