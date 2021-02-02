
SPACE = " "
TABLE_GAP = SPACE + SPACE + SPACE + SPACE
DASH = "-"
PLUS = "+"
MINUS = "-"

#arithmeticProblems, displayAnswer
# splitProblems


def arithmetic_arranger(arithemticProbs, displayAnswer=False):
    splitProbs = []
    for aProb in arithemticProbs:
        splitProbs.append(aProb.split())

    # arithemticProbs => ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    # splitProbs => [['32', '+', '8'], ['1', '-', '3801'], ['9999', '+', '9999'], ['523', '-', '49']]
    
    checkErrors(splitProbs)

    for i in range(len(splitProbs)):
        aProbSpacedLines = spaceOperandWithAnswer(splitProbs[i][0], splitProbs[i][1], splitProbs[i][2])
        # aProbSpacedLines => ['  32', '+  8', '  40'] from ['32', '+', '8']
        
        splitProbs[i][0] = aProbSpacedLines[0]
        splitProbs[i][1] = aProbSpacedLines[1]
        splitProbs[i][2] = aProbSpacedLines[2]

    dash = ""
    #
    probsBars = []
    for i in range(0, len(splitProbs)):
        for j in range(len(splitProbs[i][0])):
            dash += DASH
        probsBars.append(dash)
        dash = ""
        
    # Get something like
    # probsBars => ['----', '------', '------', '-----']
    
    return printer(splitProbs, probsBars, displayAnswer)


def printer(splitProbs, probsBars, displayAnswer):
    tableString = ""

    for i in range(len(splitProbs[0])):
        for j in range(len(splitProbs)):

            if (i == 2 and displayAnswer == False):
                continue

            if (j == 0):
                pad = ""
            else:
                pad = TABLE_GAP

            tableString += (pad + splitProbs[j][i])

        if (i == 1): tableString += "\n" + (border(probsBars))
            
        tableString += "\n"
    return tableString


def spaceOperandWithAnswer(topOperand, operator, btmOperand):
    subm = addSub(topOperand, operator, btmOperand)
    lbtm = len(btmOperand)
    ltop = len(topOperand)

    if lbtm > ltop:
        for i in range(lbtm - ltop):
            topOperand = SPACE + topOperand
    else:
        for i in range(ltop - lbtm):
            btmOperand = SPACE + btmOperand

    btmOperand = operator + SPACE + btmOperand
    topOperand = SPACE + SPACE + topOperand

    for i in range(len(btmOperand) - len(subm)):
        subm = SPACE + subm
    return [topOperand, btmOperand, subm]


def addSub(topOperand, operator, Operand):
    ans = 0
    if operator == "+":
        ans = int(topOperand) + int(Operand)
    else:
        ans = int(topOperand) - int(Operand)

    return str(ans)

 #################################


def border(probsBars):
    borderDash = ""
    for i in range(len(probsBars)):
        if (i == 0):
            pad = ""
        else:
            pad = TABLE_GAP
            
        borderDash += pad + probsBars[i]
    
    return borderDash

##############################


def checkErrors(splitProbs):
    
    if len(splitProbs) > 5:
        print("Error: Too many problems.")
        quit()

    
    for i in range(len(splitProbs)):
        
        # Operator should be + or -
        if (splitProbs[i][1] != "+" and splitProbs[i][1] != "-"):
            print("Error: Operator must be '+' or '-'.")
            quit()

        # Must be digit
        if (splitProbs[i][0].isdigit() != True or splitProbs[i][2].isdigit() != True):
            print("Error: Numbers must only contain digits.")
            quit()

        #  Must be at most 4 digit number
        if (len(splitProbs[i][0]) > 4 or len(splitProbs[i][2]) > 4):
            print("Error: Numbers cannot be more than four digits.")
            quit()

