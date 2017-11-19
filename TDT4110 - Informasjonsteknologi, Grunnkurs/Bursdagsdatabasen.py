birthdays = {"26 juli": ["Erling", "Fridtjof", "Jony"]}

def add_birthday_to_date(date, name):
    birthdays[date] = name

add_birthday_to_date("26 oktober", "Magnus")

print(birthdays)

def add_birthday_to_date ( date , name ):
    try :
        birthdays [ date ]. append ( name )
    except KeyError :
        birthdays [ date ] = name
    except AttributeError :
        birthdays [ date ] = [ birthdays [ date ][0], name ]


add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")


print(birthdays)