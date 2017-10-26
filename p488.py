#p488
#https://uva.onlinejudge.org/external/4/p488.pdf
def printNumber(num):
    for i in range(1, num + 1):
        print(num, end='')
    print()


case = 0 #case count
setList = [] #set array
#case = int(input('how many cases to input: '))
case = int(input())
print()
while case > 0:
    newset = {}
    newset['Amplitude'] = int(input())
    newset['Frequency'] = int(input())
    setList.append(newset)
    print()
    case -= 1

#output for loop
for setpair in setList:
    #print('amplitude: ' + setpair['Amplitude'])
    #print('frequency: ' + setpair['Frequency'])
    for f in range(0, setpair['Frequency']):
        for a in range(1, setpair['Amplitude'] * 2):
            if a <= setpair['Amplitude']:
                printNumber(a)
            else:
                printNumber(setpair['Amplitude'] * 2 - a)
        print()
