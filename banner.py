def banner(text):
    screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than specified width {}".
                         format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner("*")
banner("Hello dude")
banner(" ")
banner("Hello dudes")
banner("F" * 60)
banner("*")
