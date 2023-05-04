import sys


def bmi(weight, height):
    return weight / height ** 2


if __name__ == "__main__":
    weight = int(sys.argv[1])
    height = int(sys.argv[2])
    print(bmi(weight, height))