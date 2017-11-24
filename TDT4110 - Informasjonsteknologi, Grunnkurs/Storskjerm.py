def enter_line(prompt,length):
    text = ""
    while len(text) != length:
        print("The string must be " + str(length) + " characters long")
        text = input(prompt)
    print("Good job!")
#enter_line("Enter your name:",6)

def adjust_string(text,length):
    l = len(text)
    if len(text) > length:
        text = text[:length]
    elif l < length:
        text = " " * ((length - l) // 2) + text
        text += " " * (length - len(text))
    return text
print(adjust_string("Fiskepinner",5))


def enter_line_smart(prompt,length):
    something = input(prompt)
    adjust_string(something,length)
    return something

def enter_show_text():
    Content = []
    for i in range(0,6):
        text = enter_line_smart("Line" + str(i+1)+": ",30 )
    Content.append(text)