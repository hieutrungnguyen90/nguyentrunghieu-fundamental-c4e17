from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    fill(colors[i])
    begin_fill(collors[i])
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    end_fill(colors[i])

mainloop()
