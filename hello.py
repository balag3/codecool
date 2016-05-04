import sys

def greeting():
    try:
        return ("Hello %s!" %(sys.argv[1]))
    except IndexError:
        return ("Hello World!")

print (greeting())
