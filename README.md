import turtle


data = [
  {"x":69, "y":7, "rgb":"#000000"},
  {"x":70, "y":7, "rgb":"#222222"},
  {"x":71, "y":8, "rgb":"#333333"},
  {"x":72, "y":9, "rgb":"#444444"},
  {"x":68, "y":5, "rgb":"#555555"}
]


pixel_size = 20
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


for pixel in data:
    x = pixel['x'] * pixel_size
    y = pixel['y'] * pixel_size
    color = pixel['rgb']

    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

turtle.done()
