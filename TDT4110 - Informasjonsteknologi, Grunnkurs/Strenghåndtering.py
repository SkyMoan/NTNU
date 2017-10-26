string1 = 'hei'
string2 = 'hello'
string3 = 'hello'


def check_equals(str1, str2):

    return str1 is str2

print(check_equals(string2, string3))

def reversed_word(str):
    reversed = ''
    index = len(str) - 1

    while index >=0:
        reversed += str[index]
        index-=1

    return reversed

print(reversed_word(string2))
