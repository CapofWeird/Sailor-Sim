#This file handles date and time manipulation

#Checks whether the current year is a leap year
def CheckLeapYear(year):
    if ((year % 4) == 0):
        isLeapYear = True
        if ((year % 100) == 0):
            isLeapYear = False
            if ((year % 400) == 0):
                isLeapYear = True
    else:
        isLeapYear = False

    return isLeapYear


#Updates the program clock to represent the passage of time
#I sure hope I can figure out some other way to do this because
#gosh dangit it's ugly
def UpdateDateTime(currentTime, updateMinute = 0, updateHour = 0,
                    updateDay = 0, updateMonth = 0, updateYear = 0):
    MONTHS_31_DAYS = [1, 3, 5, 7, 8, 10, 12] #Months with 31 days in them
    currentTime[0] += updateMinute
    currentTime[1] += updateHour
    currentTime[2] += updateDay
    currentTime[3] += updateMonth
    currentTime[4] += updateYear
    #Are the minutes equal to or over 60?
    if (currentTime[0] >= 60):
        currentTime[0] -= 60
        currentTime[1] += 1
    #Are the hours over 24?
    if (currentTime[1] > 24):
        currentTime[1] -= 24
        currentTime[2] += 1
    #Is it a new month?
    #31 day months
    if (currentTime[3] in MONTHS_31_DAYS):
        if (currentTime[2] > 31):
            currentTime[2] -= 31
            currentTime[3] += 1
    #30 day monthes
    elif (currentTime[3] != 2):
        if (currentTime[2] > 30):
            currentTime[2] -= 30
            currentTime[3] += 1
    #February
    else:
        #Leap year February
        if (CheckLeapYear(currentTime[4])):
            if (currentTime[2] > 29):
                currentTime[2] -= 29
                currentTime[3] += 1
        #Normal year February
        else:
            if (currentTime[2] > 28):
                currentTime[2] -= 28
                currentTime[3] += 1
    #Is it a new year?
    if (currentTime[3] > 12):
        currentTime[3] -= 12
        currentTime[4] += 1
    
    return currentTime
