ukedager = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def weekday_newyear(year):
    num_leap_year = 0
    if year == 1900:
        return 0
    else:
        for i in range(1900,year):
            if is_leap_year(i):
                num_leap_year += 1
    year_count = year - 1900
    return ((year_count + num_leap_year) % 7)

def is_workday(weekday):
    return 0 <= weekday < 5

def workdays_in_year(year):
    days = 365
    num_workdays = 0
    start_day = weekday_newyear(year)
    if is_leap_year(year):
        days = 366
    for i in range(start_day, days + start_day):
        j = i % 7
        if is_workday(j):
            num_workdays += 1
    return num_workdays

for year in range (1900, 1920):
    weekday = ukedager[weekday_newyear(year)]
    num_workdays = workdays_in_year(year)
    print("%i har %i arbeidsdager og begynner på en %s" % (year, num_workdays, weekday))