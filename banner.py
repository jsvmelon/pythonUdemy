def banner(text, width):
    if len(text) > width - 4:
        raise ValueError("String {} is larger than specified width {}".
                         format(text, width))

    if text == "*":
        print("*" * width)
    else:
        output_string = "**{}**".format(text.center(width - 4))
        print(output_string)


banner("*", 80)
banner("Hello dude", 80)
banner(" ", 80)
banner("Hello dudes", 80)
banner("F" * 60, 80)
banner("*", 80)
