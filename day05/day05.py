import re

vowels = r"[a-z]*[aeiou][a-z]*[aeiou][a-z]*[aeiou][a-z]*"
threeSameChar = r"[a-z]*(a{2}|b{2}|c{2}|d{2}|e{2}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|m{2}|n{2}|o{2}|p{2}|q{2}|r{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}|z{2})[a-z]*"
notBad = r"(\w*ab\w*|\w*cd\w*|\w*pq\w*|\w*xy\w*)"

def first_star():
    output = set()
    with open('day05.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            matchVowels = re.match(vowels, line)
            matchThree = re.match(threeSameChar, line)
            matchNot = re.match(notBad, line)
            if matchVowels and matchThree and not matchNot:
                print(line + " ok")
                output.add(line)
            else:
                print(line + " ko")
        f.close()


    print(len(output))

# first_star()

twoPairs = r".*([a-z]{2}).{1,}\1.*"
efe = r".*([a-z])(?!\1)([a-z])\1.*"

combine = r".*([a-z]{2}).*([a-z])(?!\2)([a-z])\2.*\1.*"

def second_star():
    output = set()
    with open('day05.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            matchTwoPairs = re.match(combine, line)
            matchEfe = re.match(efe, line)
            if matchTwoPairs:
                print(line + " ok")
                output.add(line)
            else:
                print(line + " ko")
        f.close()


    print(len(output))

second_star()

# qjhvhtzxzqqjkmpb
# xxyxx
# uurcxstgmygtbstg
# ieodomkazucvgmuy
