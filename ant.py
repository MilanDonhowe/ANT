# Langston's Ant!
# Usage python ant.py board_size square_size delay moves


import time
from tkinter import *
import sys

if (len(sys.argv) > 4):
    MAP_SIZE, magnitude, delay, moves = map(int, sys.argv[1:])
    if MAP_SIZE % magnitude != 0:
        print("Error: square_size must be a multiple of the board_size! {MAP_SIZE} % {magnitude} == {MAP_SIZE % magnitude}, should equal 1!")
else:
    MAP_SIZE = 100
    magnitude = 5
    moves = 100
    delay = 10



window = Tk()
window.winfo_toplevel().title("ANT")


map_list = [["white" for x in range(MAP_SIZE//magnitude)] for y in range(MAP_SIZE//magnitude)]

name = Label(window, text="Langston's Ant")
name.pack()
map = Canvas(window, width=MAP_SIZE, height=MAP_SIZE)
map.pack()

class Ant:
    def __init__(self, x, y, magnitude, direction, delay):
        self.x = x
        self.y = y
        self.magnitude = magnitude
        self.direction = direction
        self.delay = delay

    def set_bbox(self):
        self.box = (self.x, self.y, self.x+self.magnitude, self.y+self.magnitude)

    def draw_self(self):
        self.set_bbox()
        map.create_rectangle(self.box, fill="red")
        map.update()

    def checkColor(self):
        if (map_list[self.y//magnitude][self.x//magnitude] == "white"):
            map_list[self.y//magnitude][self.x//magnitude] = "black"
            self.direction -= 90
            if (self.direction < 0):
                self.direction = 270
        else:
            map_list[self.y//magnitude][self.x//magnitude] = "white"
            self.direction += 90
            if (self.direction > 270):
                self.direction = 0


    def move(self):

        map.create_rectangle(self.box, fill=map_list[self.y//magnitude][self.x//magnitude])
        if (self.direction == 0):
            self.x += self.magnitude
        elif (self.direction == 90):
            self.y += self.magnitude
        elif (self.direction == 180):
            self.x -= self.magnitude
        elif (self.direction == 270):
            self.y -= self.magnitude
        else:
            print(f"ERROR: Unknown Direction, {self.direction}")
            exit()
        try:
            self.checkColor()
        except IndexError:
            print("The Ant Has Left the Board!")
            global moves
            moves = 0

def draw_map(map_list):
    y, x = 0, 0
    for row in map_list:
        x = 0
        for square in row:
            box = (x,y,x+magnitude,y+magnitude)
            map.create_rectangle(box, fill=square)
            x += magnitude
        y += magnitude


def antLoop(ant_obj):
    ant_function = moveAntObj(ant_obj)
    ant_function()

def moveAntObj(ant_obj):
    this_ant = ant_obj
    def moveAnt():
        this_ant.move()
        this_ant.draw_self()
        global moves
        moves -= 1
        if (moves > 0):
            window.after(ant_obj.delay, moveAnt)
    return moveAnt

red = Ant(MAP_SIZE//2, MAP_SIZE//2, magnitude, 180, delay)
draw_map(map_list)
red.draw_self()
antLoop(red)

window.mainloop()
