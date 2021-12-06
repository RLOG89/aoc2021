import sys
from functools import reduce

def easy(lines):
    # compare input with previous input and get count where next > previous
    count = 0
    prev = float('inf')

    for l in lines:
        if int(l) > prev:
            count += 1 
        prev = int(l)
    return count

def hard(lines):
    # split into overlapping chunks of 3 then 
    # compare totals with previous input to get count where next > previous
    count = 0
    prev = float('inf')

    def chunks(arr, length):
        for i in range(len(arr) - length):
            yield arr[i:i + (length + 1)]

    for i in chunks(lines, 2):
        total = reduce((lambda x, y: int(x) + int(y)), i)
        if total > prev:
            count += 1
        prev = total
    return count
    
if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
        a = easy(lines)
        print(a)

        b = hard(lines)
        print(b)

