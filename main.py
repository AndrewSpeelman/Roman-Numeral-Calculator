#Programmer: Andrew Speelman 
#Description: A roman numeral addition & subtraction calculator

import re
import sys

subtractiveDict = {
    "IIII" : "IV",
    "VIIII" : "IX",
    "XXXX" : "XL",
    "LXXXX" : "XC",
    "CCCC" : "CD",
    "DCCCC" : "CM"
}
newDict = {
    "IIIII" : "V",
    "VV" : "X",
    "XXXXX" : "L",
    "LL" : "C",
    "CCCCC" : "D",
    "DD" : "M",
    "IIII" : "IV",
    "VIIII" : "IX",
    "XXXX" : "XL",
    "LXXXX" : "XC",
    "CCCC" : "CD",
    "DCCCC" : "CM"
}
# Info: Function to check the operands of Roman Numerals on the rules, 
#       returning an error if a rule is broken.     
def RomanCheck(romanNum):
    pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    for numeral in romanNum:
        if not re.search(pattern, numeral):
            sys.exit("Invalid Roman Numeral.")
 
#Info: Takes user input of a roman numeral +/- equation and extracts the operands 
#      and operators into seperate variables and returns them. Also, RomanCheck is
#      called to validate that the operands are indeed roman numerals.
def stringProcess(input):
    operands = re.compile('\w+').findall(input)
    operators = re.findall(r'[\+\-*/]', input) 
    RomanCheck(operands) #make sure input is valid
    return(operands, operators)

#Info: Performs roman numeral addition without conversion to arabic values. The
#      algorithm is as follows: substitued subtractives, concatenate the operands, 
#      sort the symbols in descending value, and substitute back in the subtractives.
def romanAddition(input):
    #Substitute any subtractives, "uncompact" roman values
    for i,numeral in enumerate(input): #each operand
        for key,val in subtractiveDict.items(): #each dictionary entry
            if val in numeral:  #check dictionary
                input[i] = numeral.replace(val, key) #replace if needed 
    
    #Put all operands together -- catenate them
    combinedString = "".join(input)
    print("combined string:",combinedString)
    
    #Sort the symbols in largest on left, smallest on right notation
    order = "MDCLXVI"
    unsortedCombinedString = list(combinedString)
    sortedCombinedString = sorted(unsortedCombinedString, key = order.index)
    finalString = "".join(sortedCombinedString)
    iterator = 0
    nList = [finalString]

    #Compact the result by substituting subtractives where possible
    for key,val in newDict.items(): #each dictionary entry
        if key in nList[0]:  #check dictionary
            nList[0] = nList[0].replace(key,val)#replace if needed
        
    
    print("Answer:",nList)
 
# Description: Function that will subtract a list of roman numerals, assuming 
#              that the largest value is the first most element in list 
#              and subtracting the remainder of the list from the first
#              element. The result is printed. 
def romanSubtraction(input):
    #Substitute any subtractives, "uncompact" roman values
    for i,numeral in enumerate(input): #each operand
        for key,val in subtractiveDict.items(): #each dictionary entry
            if val in numeral:  #check dictionary
                input[i] = numeral.replace(val, key) #replace if needed 
    
    #Any symbols occurring in the second value are "crossed out" in the first.        
    for i in range(1, len(input)): #Subtractions = Operands - 1
        word = list(input[i])
        for char in word:
            if char in input[0]:
                input[0] = input[0].replace(char, "", 1)
                input[i] = input[i].replace(char, "", 1)
    print("The final subtracted answer:",input[0])

################ MAIN #######################

input1 = "CXCV + XXI + LXXXVIII"
input2 = "(CCCXCV - CXV) - LXX"
input3 = "CCMCC + LCLCMIII"

operands, operators = stringProcess(input1)

if operators[0] == "+":
    romanAddition(operands)
else:
    romanSubtraction(operands)

