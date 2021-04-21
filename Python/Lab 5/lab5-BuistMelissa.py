
#*********************************************************************
# Lab 5: <Graphics>
#
# Description:
# <This program draws a car and makes it drive
# across the screen>
#
# Author: <Melissa Buist, melissa.buist@mytwu.ca>
# Date: <Novemember 23, 2018>
#
# Input: <>
# Output: <a car graphics>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Melissa Buist>
#*********************************************************************/
from graphics import *
#add any functions or classes you might define here

class Car():

    def __init__(self, center, center2, wheel_radius, x, y, x2, y2):
        self.wheel_circle = Circle(center, wheel_radius)
        self.car_rectangle = Rectangle(Point(x, y), Point(x2, y2))
        self.wheel2_circle = Circle(center2, wheel_radius)

    def draw(self, win):  
        self.wheel_circle.draw(win)
        self.wheel2_circle.draw(win)
        self.car_rectangle.draw(win)
        

    def move(self, dx, dy): 
        self.wheel_circle.move(dx, dy)
        self.car_rectangle.move(dx,dy)
        self.wheel2_circle.move(dx,dy)

    def set_color(self, wheel_color, car_color):
        self.wheel_circle.setFill(wheel_color)
        self.car_rectangle.setFill(car_color)
        self.wheel2_circle.setFill(wheel_color)
        
    def undraw(self):  
        self.wheel_circle .undraw() 



def main():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Car', 700, 500) 

    # What we'll need for the wheel...
    wheel_center = Point(100, 450)
    wheel_radius = 30
    wheel2_center = Point(300, 450)

    # Make a wheel object
    new_car = Car(wheel_center, wheel2_center, wheel_radius, 50, 430, 350, 200)

    # Set its color
    new_car.set_color('red', 'blue')

    # And finally, draw it 
    new_car.draw(new_win)

    count = 1000

    while count != 0 :
        new_car.move(1, 0)
        count = count-1

    # Run the window loop (must be the *last* line in your code)
    new_win.mainloop()

    






main()




