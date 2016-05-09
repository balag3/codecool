
solution = []

def find_it(Alist,start,stop):
    if start > stop:
        return Alist
    x = start*start
    solution.append(x)
    return find_it(Alist,start + 1,stop)

doors = (find_it(solution,1,10))
print("The following doors are open : %s" %(doors))
