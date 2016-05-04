
starting_numbers = [0,1]

stop = input('How many fibonacci numbers do you want?')

def fill_fibonaccis(aList,aStop):
    if len(aList) < int(aStop) :
        new = aList[len(aList)-1] + aList[len(aList)-2]
        aList.append(new)
        return fill_fibonaccis(aList,aStop)
    return aList


genarated = fill_fibonaccis(starting_numbers,stop)


def pretty_print(aList):
    line = 1
    for i in aList:
        print (line,':','    ',i)
        line += 1


print (pretty_print(genarated))
