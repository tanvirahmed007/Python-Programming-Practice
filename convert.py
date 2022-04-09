def lbsToKG(weight):
    return weight * 0.45


def kgToLbs(weight):
    return weight * 2.20


def max_num(numbers):
    max_num = numbers[0]
    for item in numbers:
        if item > max_num:
            max_num = item
    return max_num