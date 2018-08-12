##L8T2

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


# Hauptfunktion
def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    if(not dateIsBefore(year1, month1, day1, year2, month2, day2)):
        return -1
    num = 0


    while(year1 < year2 or month1 < month2 or day1 < day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        num += 1

    return num


def next_day(year, month, day):
    dom = lap_year(year)

    if(month == 12 and day == 31):
        year += 1
        month = 1
        day = 1
    elif(day == dom[month-1]):
        month += 1
        day = 1
    else:
        day += 1

    return year, month, day


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2


def lap_year(year):
    # Days of month, entweder Schaltjahr oder Normaljahr
    dom_norml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dom_schalt = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # return dom_norml or dom_schalt
    if (year % 4):
        return dom_norml
    elif (year % 100):
        return dom_schalt
    elif (year % 400):
        return dom_norml
    else:
        return dom_schalt


# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


if(__name__ == '__main__'):
    test()
    """year1 = int(input("Start year: "))
    month1 = int(input("Start month: "))
    day1 = int(input("Start day: "))

    year2 = int(input("End year: "))
    month2 = int(input("End month: "))
    day2 = int(input("End day: "))
    """
    print(daysBetweenDates(2012, 1, 1, 2011, 2, 1))