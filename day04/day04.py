import hashlib

def first_star():
    base = "iwrupvqb"
    found = False
    i = 0
    while not found and i <= 609044:
        input = (base + str(i))
        hash = hashlib.md5(input.encode()).hexdigest()
        if str(hash[:5]) == "00000":
            found = True
            print(i)
        i += 1

first_star()

def second_star():
    base = "iwrupvqb"
    found = False
    i = 0
    while not found:
        input = (base + str(i))
        hash = hashlib.md5(input.encode()).hexdigest()
        if str(hash[:6]) == "000000":
            found = True
            print(i)
        i += 1

second_star()