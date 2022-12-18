_in = open("in.txt", "r")
_inDATA = _in.read()
_out = open("out.txt", "w")
_inList = _inDATA.splitlines()
quantity = _inList[0]
quantity = int(quantity)
lineAmount = quantity*2
_inList.pop(0)
NoTable = ['1 0 1','1 0 0 1','1 0 0 0 1']
print('LICZENIE...\n')
Answers = []

for x in range(quantity):
    BuildingAmount = int(_inList[0])
    _inList.pop(0)
    BuildingString = str(_inList[0])
    _inList.pop(0)
    BuildingNumbers = BuildingString.split(sep=' ')
    BuildingNumbers = [int(s) for s in BuildingNumbers]
    BuildingNumbersBin = BuildingNumbers
    BuildingNumbersBin = [1 if x != 0 else x for x in BuildingNumbersBin]
    BuildingStringBin = " ".join(map(str,BuildingNumbersBin))
    print(BuildingStringBin)
    if BuildingStringBin in NoTable:
        Answers.append("NIE")
    else:
        Answers.append("TAK")

_out.write("")
_out.mode = "a"
for y in range(quantity):
    if y != 0:
        _out.write('\n')
        y-=1
    print(y)
    print(Answers[y])
    _out.write(Answers[y])
    
print('\nKONIEC')