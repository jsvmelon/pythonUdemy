class Tag:
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" '
                         '"http://www.w3.org/TR/html4/loose.dtd"', '')
        self.end_tag = ''  # doc type doesn't have an end tag


class Head(Tag):
    def __init__(self, title=None):
        super().__init__("head", '')
        self._title = title

    def add_title(self, title):
        self._title = title

    def display(self, file=None):
        if self._title is not None:
            self.contents += "<title>{}</title>".format(self._title)
        super().display(file)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')
        self.body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)

        super().display(file)


class HtmlDoc:
    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file)
        print('<html>', file)
        self._head.display(file)
        self._body.display(file)
        print('</html>', file)


if __name__ == "__main__":
    my_page = HtmlDoc("My page's grandiose title")
    my_page.add_tag("h1", "Main Heading")
    my_page.add_tag("h2", "Secondary Heading")
    my_page.add_tag("p", "paragraph")

    with open("html_file.html", "w") as file_output:
        my_page.display(file_output)
