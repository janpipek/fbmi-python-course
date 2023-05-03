def bmi(weight, height):
    return weight / height ** 2

if __name__ == "__main__":
    weight = int(input("Weight:"))
    height = int(input("Height:"))
    print(bmi(weight, height))