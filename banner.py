def banner(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("Too long")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner("*")
banner("Hello dude")
banner(" ")
banner("Hello dudes")
banner("*")
