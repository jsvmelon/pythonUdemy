def banner(text, width=66):
    if len(text) > width - 4:
        raise ValueError("String {} is larger than specified width {}".
                         format(text, width))

    if text == "*":
        print("*" * width)
    else:
        output_string = "**{}**".format(text.center(width - 4))
        print(output_string)


banner("*")
banner("Hello dude")
banner(" ")
banner("Hello dudes")
banner("F" * 60)
banner("*")
