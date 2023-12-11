def first_step():
    global open
    with open('day01.txt') as f:
        line = f.readline()
        open = line.count("(")
        close = line.count(")")
        f.close()
        print(open - close)

first_step() #74


def second_step():
    global open
    with open('day01.txt') as f:
        line = f.readline()
        inc = 0
        open = 0
        for c in line:
            if c == '(':
                inc += 1
                open += 1
            elif c == ')' and open < 0:
                print(inc)
                break
            else:
                inc += 1
                open -= 1
        f.close()


second_step() #1795