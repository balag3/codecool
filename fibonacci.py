
##Print user given count of fibonacci numbers

#setting the starting numbers.Option 2  is [1,1]
starting_numbers = [0,1]

#asking user input for upper count of fibonacci numbers
stop = input('How many fibonacci numbers do you want?')

#fill the list recursively up to the given count
def fill_fibonaccis(aList,aStop):
    if len(aList) < int(aStop) :
        new = aList[len(aList)-1] + aList[len(aList)-2]
        aList.append(new)
        return fill_fibonaccis(aList,aStop)
    return aList


genarated = fill_fibonaccis(starting_numbers,stop)

# printing lines with the numbercount
def pretty_print(aList):
    line = 1
    for i in aList:
        print (line,':','    ',i)
        line += 1


print (pretty_print(genarated))
