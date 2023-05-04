import sys


def bmi(weight, height):
    return weight / height ** 2


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: bmi-safe.py [WEIGHT] [HEIGHT]")
        sys.exit(-1)
    try:
        weight = int(sys.argv[1])
    except ValueError:
        print(f"Weight must be an integer, not {sys.argv[1]}")
        sys.exit(-1)

    try:
        height = int(sys.argv[2])
    except ValueError:
        print(f"Height must be an interger, not {sys.argv[2]}")
        sys.exit(-1)

    print(bmi(weight, height))