def Repeater(character_to_repeat, amount):
    output = ""
    for i in range(0, amount):
        output += character_to_repeat
    return output

def Title(title):
    character = "#"
    banner = Repeater(character, len(title) + 4)
    spacer = character + Repeater(" ", len(title)+2) + character
    print(banner)
    print(spacer)
    print(character + " " + title + " " + character)
    print(spacer)
    print(banner + "\n")

if __name__== "__main__":
    Title("Hello World")
