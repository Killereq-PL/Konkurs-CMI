##################################     
try:                             #
    _in = open("in.txt", "r")    #
except FileNotFoundError:        #
    _in = open("in.txt", "w")    #
    _in.write('jeden\ndwa\ndwa') #
    _in.mode = 'r'               #
_inDATA = _in.read()             # Inicjalizacja
_out = open("out.txt", "w")      #
_inList = _inDATA.splitlines()   #
quantity = _inList[0]            #
_inList.pop(0)                   #
print('LICZENIE...\n')           #
Answers = []                     #
##################################


#miejsce na kod


######################################
_out.write("") #wyczysc plik out.txt #
_out.mode = "a"                      #
for y in range(len(Answers)):        #
    if y != 0:                       #
        _out.write('\n')             # Koniec
    print(Answers[y])                #
    _out.write(Answers[y])           #
                                     #
print('\nKONIEC')                    #
######################################