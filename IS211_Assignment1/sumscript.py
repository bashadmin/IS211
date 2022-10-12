import sys

def sumarg():
    n = 0
    sum_lst = sys.argv[1:] 
    for i in sum_lst:
        n += int(i)
    print(n)


if __name__ == "__main__":
    sumarg()