import turtle, time

pen = turtle.Turtle()
turtle.title("Happy Independence Day")

def write_heading():
    pen.color("blue")
    pen.up()
    pen.setpos(-250, 170)
    pen.down()
    pen.write("Happy Independence Day", font=("cambria", 35))

def fill_color(colour):

    pen.fillcolor(colour)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(320)
        pen.right(90)
        pen.forward(63.3)
        pen.right(90)
    pen.end_fill()


def draw_flag():
    pen.up()
    pen.setpos(-170, 100)
    pen.down()
    pen.color("black")
    
    for _ in range(2):
        pen.forward(320)
        pen.right(90)
        pen.forward(190)
        pen.right(90)
    
    fill_color("orange")
    pen.right(90)
    pen.forward(63.3+63.3)
    
    pen.left(90)
    fill_color("green")

if __name__ == "__main__":
    write_heading()
    draw_flag()
    time.sleep(4)