import tkinter


def parabola(x_input: int):
    return x_input * x_input / 100


def draw_axes(canvas: tkinter.Canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="grey")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="grey")


def plot(canvas: tkinter.Canvas, x_coord, y_coord):
    canvas.create_line(x_coord, -y_coord, x_coord + 1, -y_coord + 1, fill="red")


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas1 = tkinter.Canvas(main_window, width=320, height=480)
canvas1.grid(row=0, column=0)

canvas2 = tkinter.Canvas(main_window, width=320, height=480, background="blue")
canvas2.grid(row=0, column=1)

draw_axes(canvas1)
draw_axes(canvas2)

for x in range(-100, 101):
    plot(canvas1, x, parabola(x))

main_window.mainloop()
