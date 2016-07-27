import random

def rotateCyclic():
    size = int(random.randint(20, 50))
    p = []
    for x in range(size):
        newNum = random.randint(1, 100)
        if p.count(newNum) < 1:
            p.append(newNum)
    p.sort()
    q = []
    clip = random.randint(1, len(p))
    # print(p, clip)
    for c in range(clip):
        q.append(p.pop())
    q.sort()
    print(p)
    print(q)

    for ele in p:
        q.append(ele)

    print(q)
    return q

def getMax(inputVal, low, high):
    sz = (high - low)
    print("size of input is " + str(sz))
    mid = int((low + high)/2)
    if sz == 1:
        return low
    elif inputVal[low] > inputVal[mid]:
        # look at 1st half
        return getMax(inputVal, low, mid)
    else:
        # look at 2nd half
        return getMax(inputVal, mid, high)





def main():
    print("Find min in a cyclic sorted integers")
    inputVal = rotateCyclic()
    p = getMax(inputVal, 0, len(inputVal))
    print("Max value is " + str(inputVal[p]))
    print("Min value is " + str(inputVal[(p+1)%len(inputVal)]))

if __name__ == "__main__":
    main()
