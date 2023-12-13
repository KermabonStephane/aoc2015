

def first_step():
    with open('day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            open_count = line.count("(")
            close_count = line.count(")")
            print(open_count - close_count)
        f.close()

first_step() #74


def second_step():
    with open('day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            inc = 0
            open_count = 0
            for c in line:
                if c == '(':
                    inc += 1
                    open_count += 1
                elif c == ')' and open_count < 0:
                    print(inc)
                    break
                else:
                    inc += 1
                    open_count -= 1
        f.close()


second_step() #1795