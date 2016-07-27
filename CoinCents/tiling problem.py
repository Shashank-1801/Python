import random

X = []
Y = []
def getoneX():
    f  = int(random.randint(2, 100))
    s = int(random.randint(0, f))
    #print(s)
    #print(f)
    x = (s,f)
    #print(x)
    return x

def generateX():
    for s in range(20):
        X.append(getoneX())


def outputX():
    for s in range(20):
        print(X[s])
    print("max is " + str(max(X, key=lambda t: t[1])))


def tiling():
    while len(X) != 0:
        end = max(X, key=lambda t: t[1])
        f = end[1]
        start =[]
        toberemoved =[]
        # looking for an finish time >= to the chosen time
        for x in X:
            if x[1] >= f:
                start.append(x)
        elem = min(start, key=lambda t: t[0])
        elemStart = elem[0]
        Y.append(elem)
        #print(elem)
        # remove all elements which has start time greater or equal than element chosen
        for x in X:
            if x[0] >= elemStart:
                toberemoved.append(x)
        for p in toberemoved:
            X.remove(p)
        #end = elem
    Y.reverse()
    print("Final set is : " + str(len(Y)))
    print(Y)


def main():
    print("Tiling problem solution")
    generateX()
    outputX()
    tiling()


if __name__ == "__main__":
    main()
