

class CalculatorGCD:
    """
    A class：calculate the greatest common divisor of two positive integers
    using the Euclidean algorithm
    """
    
    
    def __init__(self, a: int, b: int):
        """
        Initialize the instance
        """
        self.a = a
        self.b = b
        
    def calculate_gcd(self):
        """
        calculate the greatest common divisor of two positive integers
        using the Euclidean algorithm
        """
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b # Constantly update the values of a and b
        return a

def input_check(value):
    """
    Check whether the input is a positive integer.
    """
    return value.isdigit() and int(value) > 0 # The function returns True only if value is both a numeric character and greater than zero

def get_input(prompt):
    """
    Requires the user to enter a valid positive integer
    """
    while True: # Keep requesting input from the user until the function gets a valid input
        user_input = input(prompt)
        if input_check(user_input): # Check whether the input is a valid positive integer
            return int(user_input)
        else:
            print("Invalid input, please enter a positive integer.")

def main():
    """
    Enter two positive integers and calculate their GCD
    """
    # Get user input
    a = valid_input1("Please enter the first positive integer a: ")
    b = valid_input2("Please enter the second positive integer b: ")

    # Create instance and calculate GCD
    calculator = CalculatorGCD(a, b)
    gcd = calculator.calculate_gcd()

    # Output
    print(f"The greatest common divisor of {a} and {b} is {gcd}.")
    
if __name__ == "__main__":
    main()

