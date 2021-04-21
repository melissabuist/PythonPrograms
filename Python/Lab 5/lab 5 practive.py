from graphics import *
WIDTH, HEIGHT = 400, 700
RADIUS = 40





def main():
    win = GraphWin('Lab Four', WIDTH, HEIGHT)

    center = Point(100, 450)
    circ1 = Circle(center, 30)
    circ1.setFill('red')
    circ1.draw(win)

    center = Point(300, 450)
    circ2 = Circle(center, 30)
    circ2.setFill('red')
    circ2.draw(win)

    
    rect = Rectangle(Point(50, 430), Point(350, 200))
    rect.setFill('blue')
    rect.draw(win)
    for i in range(1, 40):
            circ1.move (0, 20)
            

main()
main()
