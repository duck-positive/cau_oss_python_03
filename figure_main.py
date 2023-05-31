import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please Input positive number")

myline.set_length(20, 30)
width, height = myline.get_length()
# implement exception handler
try:
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("please Input positive number")

myline.set_length(30, 40)
width, height = myline.get_length()
# implement exception handler
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please Input positive number")