import re

while True:
    myWord = input("Please enter any word ")

    if not re.match("[a-zA-Z]+", myWord):
        print("I did not understand that.  Please enter just lower or upper-case letters")
        continue

    print(myWord)


    pattern = r"[aeiouAEIOU]"
    patternA = r"[aA]"
    patternE = r"[eE]"
    patternI = r"[iI]"
    patternO = r"[oO]"
    patternU = r"[uU]"

    results = re.findall(pattern, myWord)
    print("The following vowels were found: ", "\n", results)
    print("Total number of matches = ", len(results))

    resultsA = re.findall(patternA, myWord)
    if resultsA == None:
        print("a = no match")
    else: print("a = ", len(resultsA))

    resultsE = re.findall(patternE, myWord)
    if resultsE == None:
        print("e = no match")
    else: print("e = ", len(resultsE))

    resultsI = re.findall(patternI,myWord)
    if resultsI == None:
        print("i = no match")
    else: print("i = ",len(resultsI))

    resultsO = re.findall(patternO,myWord)
    if resultsO == None:
        print("o = no match")
    else: print("o = ",len(resultsO))

    resultsU = re.findall(patternU,myWord)
    if resultsU == None:
        print("u = no match")
    else: print("u = ", len(resultsU))

    break
