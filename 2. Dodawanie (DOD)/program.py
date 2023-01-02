################################
_in = open("in.txt", "r")      #
_inDATA = _in.read()           #
_out = open("out.txt", "w")    #
_inList = _inDATA.splitlines() #
quantity = _inList[0]          # Inicjalizacja
quantity = int(quantity)       #
_inList.pop(0)                 #
print('LICZENIE...\n')         #
Answers = []                   #
################################

#miejsce na kod

######################################
_out.write("") #wyczysc plik out.txt #
_out.mode = "a"                      #
for y in range(quantity):            #
    if y != 0:                       #
        _out.write('\n')             # Koniec
    print(Answers[y])                #
    _out.write(Answers[y])           #
                                     #
print('\nKONIEC')                    #
######################################