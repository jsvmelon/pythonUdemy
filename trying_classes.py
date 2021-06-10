class Beast:
    name: str

    def __init__(self, name):
        self.name = name


unicorn = Beast("unicorn")
bear = Beast("bear")
Beast.name = "Moose"
Beast.asdf = 3

print(unicorn.name)
print(bear.name)
print(Beast.name)
print(Beast.asdf)
