from math import sqrt
from tkinter import Canvas, Tk
from numpy import arange


def parabola(page: Canvas, size: int) -> None:
    for x in arange(0, size, 0.5):
        y = x * x / size
        plot_point(page, x, y)
        plot_point(page, -x, y)


def circle(page: Canvas, radius: int, g: int, h: int, colour="red") -> None:
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=1)
    # resolution = 0.01
    # for x in arange(g, g + radius, resolution):
    #     y = h + (sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot_point(page, x, y)  # top right
    #     plot_point(page, x, 2 * h - y)  # bottom right
    #     plot_point(page, 2 * g - x, y)  # top left
    #     plot_point(page, 2 * g - x, 2 * h - y)  # bottom left


def draw_axes(page: Canvas):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="grey")
    page.create_line(0, y_origin, 0, -y_origin, fill="grey")


def plot_point(page: Canvas, x_coord, y_coord):
    page.create_line(x_coord, -y_coord, x_coord + 1, -y_coord, fill="red")


def create_coordinate_system():
    window = Tk()
    window.title("Parabola")
    window.geometry("640x480")

    page = Canvas(window, width=640, height=480)
    page.grid(row=0, column=0)

    draw_axes(page)
    return page, window


canvas, main_window = create_coordinate_system()

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0, colour="black")

main_window.mainloop()
