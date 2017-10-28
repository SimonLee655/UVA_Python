#p10107
#https://uva.onlinejudge.org/external/101/p10107.pdf
inputArray = []
while True:
    inputArray.append(int(input()))
    inputArray.sort()
    output = 0
    arrayLen = len(inputArray)
    if arrayLen % 2: #odd
        output = str(inputArray[(arrayLen - 1) // 2])
    else:
        output = str((int(inputArray[(arrayLen - 1) // 2]) + int(inputArray[(arrayLen + 1) // 2])) // 2)
    print(output)
