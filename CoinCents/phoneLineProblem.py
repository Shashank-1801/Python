import random
O = []
P = []
temp = []
size = 16


def equalObject(obj1, obj2):
	if obj1 == obj2:
		temp.append(obj1)
		return True
	else:
		return False


def findequivalence(start, end):
	if end <= start + 1:
		equalObject(P[start], P[end])
	else:
		start1 = start
		end1 = int((start+end-1)/2)
		start2 = end1 + 1
		end2 = end
		findequivalence(start1, end1)
		findequivalence(start2, end2)



def objectgenerator():
	for x in range(0, size):
		val = int(random.randint(0, 1))
		O.append(val)


def main():
	global size
	print("Find if n/2 objects are the same out of n objects")
	objectgenerator()
	for x in range(size):
		print(str(x) + "  :  " + str(O[x]))
	count1 = 0
	for x in range(size):
		if O[x] == 1:
			count1 += 1
	print("Count of 1 is " + str(count1))
	print("Count of 0 is " + str(size - count1))
	for x in range(0, size):
		P.append(O[x])
	while True:
		findequivalence(0, size-1)
		if len(temp) <= 1:
			break
		size = len(temp)
		del P[:]
		for x in range(0, size):
			P.append(temp[x])
		del temp[:]
	if len(temp) == 1:
		print("True")
	else:
		print("False")



if __name__ == "__main__":
	main()