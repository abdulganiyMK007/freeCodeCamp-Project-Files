    # add_time("3:00 AM", "2:32", "Monday")
def add_time(startTime, durationPlus, day = ""):
    # print(startTime + ', ' + durationPlus +' '+ day)
    startTimeOnly = startTime.split()             # ['3:00', 'PM']
    startTimeSplit = startTimeOnly[0].split(":")  # ['3', '00']
    durationPlusSplit = durationPlus.split(":")   # ['2', '32']
    
    # ['3', '00'],  ['2', '32'], ['PM'] => [6, 10, 'PM', 0]
    newTimeValues = getNewTime(startTimeSplit, durationPlusSplit, startTimeOnly[1])
    
    
    dayCount = newTimeValues[3]
    if (newTimeValues[3] == 0):
       endQuote = ""
    elif (newTimeValues[3] == 1):
         endQuote = "(next day)"
    else:
        endQuote = "(" + str(dayCount) + " days later)"
    
        
    return str(newTimeValues[0]) + ":" + str(newTimeValues[1]) + " " + str(newTimeValues[2]) + getDayString(day, dayCount) + " " + endQuote

##############################
def getDayString(dayStr, dayCount):
    if dayStr == "":
        return ""
        
    dayStr = dayStr.capitalize()
    
    dayList = [["SUNDAY", 0], ["MONDAY", 1],
    ["TUESDAY", 2], ["WEDNESDAY", 3],
    ["THURSDAY", 4], ["FRIDAY", 5], ["SATURDAY", 6]]
    
    dayNum = -1
    for i in range(7):
        if (dayStr == dayList[i][0].capitalize()):
            dayNum = dayList[i][1]
            break
            
    dayNum += dayCount
    while (dayNum >= 7):
        dayNum -= 7
    
    return ", " + dayList[dayNum][0].capitalize()

############################
# ['3', '00'],  ['3', '00'], ['PM'] => 
def getNewTime(startTime, durationPlus, clockFormat):
    dayCount = 0
    if (clockFormat == "PM"):
        startTime[0] = int(startTime[0]) + 12
        
    hr = int(startTime[0]) + int(durationPlus[0])
    min = int(startTime[1]) + int(durationPlus[1])
    
    if (min > 60):
        hr += 1
        min -= 60
 
    while (hr >= 24):
        hr -= 24
        dayCount += 1
    
    if (hr > 12):
        clockFormat = "PM"
        hr -= 12
    else:
        clockFormat = "AM"
        
    if (hr == 0):
        hr = 12
    
    if (min < 10):
        min = "0" + str(min)
        
    return [hr, min, clockFormat, dayCount]
 


