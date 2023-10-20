class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        prime_numbers = list(filter(lambda x: self.is_prime(x), self.numbers))
        return prime_numbers


try:
    input_numbers = list(map(int, input("Enter numbers: ").split()))
    prime_filter = PrimeFilter(input_numbers)
    filtered_primes = prime_filter.filter_primes()
    print("Prime numbers:", filtered_primes)
except ValueError:
    print("Error")
