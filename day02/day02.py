from functools import reduce


def first_step():
    result = 0
    with open('day02.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            dims = [int(x) for x in line.split('x')]
            result += dims[0] * dims[1] * 2 + dims[1] * dims[2] * 2 + dims[0] * dims[2] * 2 + min(dims[0] * dims[1], dims[1] * dims[2],  dims[0] * dims[2])
        f.close()
    print(result)


first_step()  # 1606483


def second_step():
    result = 0
    with open('day02.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            dims = [int(x) for x in line.split('x')]
            result += dims[0] * dims[1] * dims[2]
            dims.remove(max(dims))
            result += 2 * reduce(lambda x, y: x + y, dims)
        f.close()

    print(result)


second_step()  # 659
