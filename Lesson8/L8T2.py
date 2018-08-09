##L8T2

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

# Days of month, entweder Schaltjahr oder Normaljahr
dom_norml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dom_schalt = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Hauptfunktion
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    global dom_norml
    global dom_schalt
    num = 0

    if(lap_year(year2)):
        dom = dom_schalt
    else:
        dom = dom_norml

    # alle Tage des aktuellen Jahres werden zusammengerechnet
    num += day2 - 1
    for i in range(0, month2 - 1):
        num += dom[i]

    if (lap_year(year1)):
        dom = dom_schalt
    else:
        dom = dom_norml

    # alle Tage des Startjahres werden zusammengerechnet
    num -= day1 - 1
    for i in range(0, month1 - 1):
        num -= dom[i]

    # hinzuaddieren der anderen Jahre
    while(year1 < year2):
        if (lap_year(year1)):
            num += 366
        else:
            num += 365
        year1 += 1

    return num


# lap_year entscheidet ob das jeweilige jahr ein schaltjahr ist
def lap_year(year):
    if (year % 4):
        return False
    elif (year % 100):
        return True
    elif (year % 400):
        return False
    else:
        return True

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

test()