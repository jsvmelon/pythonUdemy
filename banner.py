def banner(text=" ", width=66):
    """
    Function that prints text given inside a surrounding banner of '**'
    Without any parameter a surrounded empty line will be printed.
    :param text: The text to be printed. Default is the empty string.
    :param width: The width of a banner line, default is 66
    :return: None
    """
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
banner(width=70)
banner("Hello dudes")
banner("F" * 60)
banner("*")
