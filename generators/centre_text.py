def centre_text(*args):

    # original code that we are rewriting
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "

    # does not work because arguments can have a non-string type
    # text = "-".join(args)

    text = " ".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")