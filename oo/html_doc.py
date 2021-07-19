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
    def __init__(self, doc_type=None, head=None, body=None, title=None):
        # composition and aggregation is now possible
        if doc_type is None:
            self._doc_type = DocType()
        else:
            self._doc_type = doc_type

        if head is None:
            self._head = Head(title)
        else:
            self._head = head

        if body is None:
            self._body = Body()
        else:
            self._body = body

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

    new_body = Body()
    new_body.add_tag("h1", "Aggregation")
    new_body.add_tag("p", "Unlike <strong>composition</strong>, aggregation uses existing instances"
                     " of objects to build up another object.")
    new_body.add_tag("p", "The composed objects doesn't own the objects it is composed of.")

    new_doc_type = DocType()
    new_header = Head("Aggregation document")
    my_page = HtmlDoc(doc_type=new_doc_type, head=new_header, body=new_body)
    # give our document new content by switching it's body

    my_page._body = new_body
    with open("html_file2.html", "w") as test_doc:
        my_page.display(file=test_doc)
