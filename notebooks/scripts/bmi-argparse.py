# bmi-argparse
# (thanks, chatgpt)
import argparse

def bmi(weight, height):
    return weight / height ** 2

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Calculate BMI')

    # Add arguments
    parser.add_argument('weight', type=int, help='Weight in kilograms')
    parser.add_argument('height', type=int, help='Height in centimeters')

    # Parse the arguments
    args = parser.parse_args()

    # Access the parsed values
    weight = args.weight
    height = args.height / 100  # ChatGPT forget to divide

    # Calculate BMI
    print(bmi(weight, height))