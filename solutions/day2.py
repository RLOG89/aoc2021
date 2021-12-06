import sys

def easy(lines):
    # get total of forward plus difference between up and down
    x = 0
    y = 0
    for line in lines: 
        key, value = line.split(" ")
        value = int(value)
        if key == 'forward':
            x += value
        elif key == 'up':
            y -= value
        elif key == 'down':
            y += value
    
    return x * y

def hard(lines):
    aim = 0
    x = 0
    y = 0 

    for line in lines: 
        key, value = line.split(" ")
        value = int(value)
        if key == 'up':
            aim -= value
        elif key == 'down':
            aim += value
        elif key == 'forward':
            y += value
            x += value * aim
    return x * y

if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
        a = easy(lines)
        print(a)

        b = hard(lines)
        print(b)
