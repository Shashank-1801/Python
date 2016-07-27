def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def main():
    print("Ratio between 2 fib numbers")
    for x in range(2, 100):
        p = fib(x-1)
        q = fib(x)
        print(p/q)

if __name__ == "__main__":
    main()
