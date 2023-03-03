
import turtle                    
import time


wn = turtle.Screen()                     
wn.bgcolor("black")                       
wn.title("ADFS Maze Solving Program")
wn.setup(1300,700)                        
start_x = 0
start_y = 0
end_x = 0
end_y = 0

class Maze(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("blue")             
        self.penup()                    
        self.speed(0.5)                   

class Green(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class White(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)  
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):          
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid0 = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

def setup_maze(grid):                          
    global start_x, start_y, end_x, end_y      
    for y in range(len(grid)):                 
        for x in range(len(grid[y])):          
            character = grid[y][x]             
            screen_x = -588 + (x * 24)         
            screen_y = 288 - (y * 24)          

            if character == "+":                   
                maze.goto(screen_x, screen_y)      
                maze.stamp()                       
                walls.append((screen_x, screen_y)) 

            if character == " ":                    
                path.append((screen_x, screen_y))   

            if character == "e":                    
                yellow.goto(screen_x, screen_y)     
                yellow.stamp()                      
                end_x, end_y = screen_x, screen_y   
                path.append((screen_x, screen_y))   

            if character == "s":                       
                start_x, start_y = screen_x, screen_y  
                red.goto(screen_x, screen_y)           

def search(x,y):
    frontier.append((x, y))                            
    solution[x, y] = x, y                              
    while len(frontier) > 0:                           
        time.sleep(0)                                  
        current = (x,y)                                

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            cellleft = (x - 24, y)
            solution[cellleft] = x, y  
            white.goto(cellleft)        
            white.stamp()               
            frontier.append(cellleft)  

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            celldown = (x, y - 24)
            solution[celldown] = x, y  
            white.goto(celldown)
            white.stamp()
            frontier.append(celldown)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            
            cellright = (x + 24, y)
            solution[cellright] = x, y  
            white.goto(cellright)
            white.stamp()
            frontier.append(cellright)

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            cellup = (x, y + 24)
            solution[cellup] = x, y  
            white.goto(cellup)
            white.stamp()
            frontier.append(cellup)
            
        if current == (end_x,end_y):
         break
        x, y = frontier.pop()           
        visited.append(current)         
        green.goto(x,y)                 
        green.stamp()                   
        if (x,y) == (end_x, end_y):     
            yellow.stamp()              
        if (x,y) == (start_x, start_y): 
            red.stamp()                 

def backRoute(x, y):                       
    yellow.goto(x, y)                      
    yellow.stamp()
    while (x, y) != (start_x, start_y):    
        yellow.goto(solution[x, y])        
        yellow.stamp()                     
        x, y = solution[x, y]              


maze = Maze()
red = Red()
white = White()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
frontier = []
solution = {}

setup_maze(grid0)                       
search(start_x, start_y)                
backRoute(end_x, end_y)                 
count=0
for i in  visited: 
    count+=1
print("the nodes explored are "+str(count))
wn.exitonclick()                        
    