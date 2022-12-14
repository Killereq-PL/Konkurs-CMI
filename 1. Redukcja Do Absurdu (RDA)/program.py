_in = open("in.txt", "r")
_inDATA = _in.read()
_out = open("out.txt", "w")
_inList = _inDATA.splitlines()
quantity = _inList[0]
quantity = int(quantity)
lineAmount = quantity*2
_inList.pop(0)

_out.write("")
_out.mode = "a"
for y in range(0, lineAmount):
    if y != 0:
        _out.write('\n')
    _out.write(_inList[y])