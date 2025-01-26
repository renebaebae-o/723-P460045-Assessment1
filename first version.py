
class CalculatorGCD:
    """
    A class to calculate the greatest common divisor of two positive integers
    using the Euclidean algorithm.
    """
    
    def __init__(self, a: int, b: int):
        """
        Initialize the instance with two positive integers.
        """
        self.a = a
        self.b = b
        
    def calculate_gcd(self):
        """
        Calculate the greatest common divisor of two positive integers
        using the Euclidean algorithm.
        """
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b  # Constantly update the values of a and b
        return a
    
    def new_numbers(self, a: int, b: int):
        """
        Set two new positive integers to calculate GCD.
        """
        self.a = a
        self.b = b
