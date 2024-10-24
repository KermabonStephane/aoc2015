def first_step():
    with open('day01.txt') as f:
        line = f.readline()
        left = line.count("(")
        right = line.count(")")
        print(left - right)

first_step() #74

def second_step():
    with open('day01.txt') as f:
        line = f.readline()
        inc = 0
        left = 0
        for c in line:
            if c == '(':
                inc += 1
                left += 1
            elif c == ')' and left < 0:
                print(inc)
                break
            else:
                inc += 1
                left -= 1
        f.close()

second_step() #1795