class Struct:
    def __init__(self, arr):
        self.arr = arr

    def max_number(self):
        return max(self.arr)

    def min_number(self):
        return min(self.arr)

    def first_num(self):
        return self.arr[0]

    def last_num(self):
        return self.arr[-1]

    def number_of_prime_numbers(self):
        count = 0
        for element in self.arr:
            if element == 2:
                prime = True
            elif element < 2 or not element % 2:
                prime = False
            else:
                prime = not any(element % i == 0 for i in range(3, int(element**0.5) + 1, 2))

            if prime:
                count += 1
        return count

    def number_of_even_numbers(self):
        count = 0
        for element in self.arr:
            if element % 2 == 0:
                count += 1
            else:
                continue
        return count

    def number_of_odd_numbers(self):
        count = 0
        for element in self.arr:
            if not element % 2 == 0:
                count += 1
            continue
        return count

    def __str__(self):
        return f'struc: {self.arr}'
