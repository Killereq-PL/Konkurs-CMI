_in = open("in.txt", "r")
_inDATA = _in.read()
_out = open("out.txt", "w")
_inList = _inDATA.splitlines()
quantity = _inList[0]
quantity = int(quantity)
lineAmount = quantity*2
_inList.pop(0)
print('LICZENIE...\n')

for x in range(quantity):
    BuildingAmount = _inList[0]
    _inList.pop(0)
    BuildingString = str(_inList[0])
    _inList.pop(0)
    BuildingNumbers = BuildingString.split(sep=' ')
    BuildingNumbers = [int(s) for s in BuildingNumbers]
    print(*BuildingNumbers)


_out.write("")
_out.mode = "a"
#for y in range(quantity):
#    if y != 0:
#        _out.write('\n')
#    _out.write(_inList[y])
#    print(_inList[y])
print('\nKONIEC')