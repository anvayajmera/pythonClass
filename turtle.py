import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Art")

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "white", "cyan"]

t = turtle.Turtle()
t.speed(0)
t.width(2)

for i in range(100):
    t.color(random.choice(colors))
    t.forward(i * 2)
    t.right(45)

def draw_star(size, color):
    star = turtle.Turtle()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
    star.hideturtle()

def draw_circle(radius, color):
    circle = turtle.Turtle()
    circle.color(color)
    circle.width(2)
    circle.circle(radius)
    circle.hideturtle()

def draw_square(size, color):
    square = turtle.Turtle()
    square.color(color)
    for _ in range(4):
        square.forward(size)
        square.right(90)
    square.hideturtle()

for _ in range(5):
    draw_star(random.randint(20, 100), random.choice(colors))

for _ in range(5):
    draw_circle(random.randint(50, 150), random.choice(colors))

for _ in range(5):
    draw_square(random.randint(50, 150), random.choice(colors))

def draw_spirograph(radius):
    spirograph = turtle.Turtle()
    spirograph.speed(0)
    spirograph.color(random.choice(colors))
    for _ in range(36):
        spirograph.circle(radius)
        spirograph.right(10)
    spirograph.hideturtle()

for _ in range(3):
    draw_spirograph(random.randint(50, 150))

def random_walk(turtle, steps):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.color(random.choice(colors))
        turtle.forward(20)
        turtle.setheading(random.choice(directions))

walker = turtle.Turtle()
walker.speed(0)
walker.width(2)
random_walk(walker, 200)

def draw_flower():
    flower = turtle.Turtle()
    flower.speed(0)
    flower.color(random.choice(colors))
    for _ in range(36):
        for _ in range(2):
            flower.circle(100, 60)
            flower.left(120)
        flower.left(10)
    flower.hideturtle()

draw_flower()

def draw_hexagon(size, color):
    hexagon = turtle.Turtle()
    hexagon.color(color)
    for _ in range(6):
        hexagon.forward(size)
        hexagon.right(60)
    hexagon.hideturtle()

for _ in range(5):
    draw_hexagon(random.randint(50, 150), random.choice(colors))

def draw_mandala(size):
    mandala = turtle.Turtle()
    mandala.speed(0)
    mandala.color(random.choice(colors))
    for _ in range(6):
        mandala.circle(size)
        mandala.right(60)
    mandala.hideturtle()

for _ in range(3):
    draw_mandala(random.randint(50, 150))

screen.mainloop()
