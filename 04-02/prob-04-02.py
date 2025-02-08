class CatalanNumberCalculator:
    def __init__(self, n):
        self.n = n

    """Calculate the factorial of a number."""
    def factorial(self, n):
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
            
    """Calculating the number of ways using the Catalan number formula."""
    def count_ways(self):
        numerator = self.factorial(2 * self.n)
        denominator = self.factorial(self.n + 1) * self.factorial(self.n)
        no_of_ways = numerator // denominator
        return no_of_ways


# Input from the user
n = int(input("Enter the value of n: "))

calculator = CatalanNumberCalculator(n)

print(f"The number of ways for n = {n} is: {calculator.count_ways()}")