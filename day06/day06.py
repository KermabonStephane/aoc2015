from bitarray import bitarray


def first_star():
    # initialize byte array
    bits = []
    for i in range(1000):
        bits.append(bitarray(1000))


    with open('day06.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())
            line = line.strip()
            if line.startswith("turn on "):
                zone = read_zone(line[8:])
#                print("turn on " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] = True
            elif line.startswith("turn off "):
                zone = read_zone(line[9:])
#                print("turn off " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] = False
            elif line.startswith("toggle "):
                zone = read_zone(line[7:])
#                print("toggle " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] = not bits[y][x]
        f.close()

    lit = 0
    for i in range(1000):
        lit += str(bits[i]).count("1")
#        print(str(bits[i]))

    print("lit " + str(lit))

def second_star():
    # initialize byte array
    bits = []
    for i in range(1000):
        bits.append([0] * 1000)

    with open('day06.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
 #           print(line.strip())
            line = line.strip()
            if line.startswith("turn on "):
                zone = read_zone(line[8:])
#                print("turn on " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] += 1
            elif line.startswith("turn off "):
                zone = read_zone(line[9:])
#                print("turn off " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] = max(bits[y][x] - 1, 0)
            elif line.startswith("toggle "):
                zone = read_zone(line[7:])
#                print("toggle " + str(zone[0]) + "," + str(zone[1]) + " through " + str(zone[2]) + "," + str(zone[3]))
                for x in range(zone[0], zone[2] + 1):
                    for y in range(zone[1], zone[3] + 1):
                        bits[y][x] += 2
        f.close()

    lit = 0
    for x in range(1000):
        for y in range(1000):
            lit += bits[y][x]

    print("lit " + str(lit))

def read_zone(line: str):
#    print("read zone " + line)
    element = line.split(" ")
    start = element[0].split(",")
    end = element[2].split(",")
    return min(int(start[0]), int(end[0])), min(int(start[1]), int(end[1])), max(int(start[0]), int(end[0])), max(int(start[1]), int(end[1]))

#read_zone_turn_on("turn on 5,498 through 203,835")
#first_star()
second_star()