def center_text(*args, sep=" ") -> str:
    text = ""
    for index, arg in enumerate(args):
        text += str(arg)
        if index < len(args)-1:
            text += sep
    text = str(text)
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text
    # print(" " * left_margin, text, end=end, file=file, flush=flush)


with open("menu.txt", "w") as menu:
    print(center_text("Spam with eggs"), file=menu)
    print(center_text("spam, spam, and eggs"), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    print(center_text(12), file=menu)
    print(center_text("first", "three", 3, 4, "spam", sep=";"), file=menu)
