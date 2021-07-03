jabber = open("./sample.txt", mode='r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

# using with removes the need to close() the file and avoids errors
with open("sample.txt", mode='r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

# more verbose variant
with open("sample.txt", mode='r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# using readLines() and avoiding the while loop
with open("sample.txt", mode='r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')

# back to front this time
with open("sample.txt", mode='r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

# this time reverse read of single characters
with open("sample.txt", mode='r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
