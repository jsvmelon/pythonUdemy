# import the whole module
# import turtle

# only import specific functions from a module
# from turtle import forward, right, done

# this string will be hidden
done = "Well done"

# not recommended as imported names may hide local ones
from turtle import *

forward(150)
right(250)
circle(75)
forward(150)

done()

# this will print the function reference instead of the string
print(done)
