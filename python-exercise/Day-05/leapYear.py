year = int(input('Enter year..: '))
leap = False

def leap_year (year):
    if year % 400 == 0 and year % 100 == 0:
        print('{0} is a leap year'.format(year))
    elif year % 4 == 0 and year % 100 != 0:
        print('{0} is a leap year'.format(year))
    else:
        print('{0} is a Not leap year'.format(year))
    return leap
print(leap_year(year))