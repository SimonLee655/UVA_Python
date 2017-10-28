#p10038
#https://uva.onlinejudge.org/external/100/p10038.pdf
'''A sequence of n > 0 intergers is called a jolly jumper if the absolute values of the difference between
successive elements take on all the values 1 through n - 1. For instance,

1 4 2 3

absolute value: 3 2 1

4: 1 4 2 3   => jolly
5: 1 4 2 -1 6 => not jolly

'''

def printArray(array):
    for d in array:
        print(d)
def checkJolly(array):
    isJolly = True
    arrayLen = len(array)
    for idx, val in enumerate(array):
        if idx + 1 != int(val):
            isJolly = False
            break
    return isJolly


originalInput = input()
inputArray = originalInput.split(' ')
numbersCount = inputArray.pop(0)
absArray = []
arrayLen = len(inputArray)
for idx, val in enumerate(inputArray):
    if idx != arrayLen - 1:
        absArray.append(abs(int(val) - int(inputArray[idx + 1])))
absArray.sort()

printArray(absArray)
print(checkJolly(absArray))
