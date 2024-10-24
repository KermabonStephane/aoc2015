def first_step():
    houses = set()
    houses.add((0,0))
    with open('day03.txt') as f:
        line = f.readline()
        ordinate = 0
        abscissa = 0
        for c in line:
            if c == "^":
                abscissa += 1
            elif c == ">":
                ordinate += 1
            elif c == "<":
                ordinate -= 1
            elif c == "v":
                abscissa -= 1
            houses.add((ordinate, abscissa))
    print(len(houses))

first_step()

def second_step():
    houses = set()
    houses.add((0, 0))
    with open('day03.txt') as f:
        line = f.readline()
        ordinateSanta = 0
        abscissaSanta = 0
        ordinateRobot = 0
        abscissaRobot = 0
        inc = 0
        for c in line:
            if c == "^":
                if inc % 2 == 0:
                    abscissaSanta += 1
                    houses.add((ordinateSanta, abscissaSanta))
                else:
                    abscissaRobot += 1
                    houses.add((ordinateRobot, abscissaRobot))
            elif c == ">":
                if inc % 2 == 0:
                    ordinateSanta += 1
                    houses.add((ordinateSanta, abscissaSanta))
                else:
                    ordinateRobot += 1
                    houses.add((ordinateRobot, abscissaRobot))
            elif c == "<":
                if inc % 2 == 0:
                    ordinateSanta -= 1
                    houses.add((ordinateSanta, abscissaSanta))
                else:
                    ordinateRobot -= 1
                    houses.add((ordinateRobot, abscissaRobot))
            elif c == "v":
                if inc % 2 == 0:
                    abscissaSanta -= 1
                    houses.add((ordinateSanta, abscissaSanta))
                else:
                    abscissaRobot -= 1
                    houses.add((ordinateRobot, abscissaRobot))
            inc += 1
    print(len(houses))


second_step()
