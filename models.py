from pathlib import Path, PurePath
import json
import time

BASE_DIR = Path(__file__).resolve().parent


class Struct:
    """Outgoing data structure"""

    def __init__(self, arr):
        """ This is the docstring of the class initializer, as initial parameter it has a list """
        self.arr = arr

    def max_number(self):
        """ Method to calculate the maximum value of the list """
        return max(self.arr)

    def min_number(self):
        """Method to calculate the minimum value of the list"""
        return min(self.arr)

    def first_num(self):
        """Method to calculate the first value of the list"""
        return self.arr[0]

    def last_num(self):
        """Method to calculate the last value of the list"""
        return self.arr[-1]

    def number_of_prime_numbers(self):
        """Method to calculate how many prime numbers are in the list"""
        count = 0
        for element in self.arr:
            if element == 2:
                prime = True
            elif element < 2 or not element % 2:
                prime = False
            else:
                prime = not any(element % i == 0 for i in range(3, int(element ** 0.5) + 1, 2))

            if prime:
                count += 1
        return count

    def number_of_even_numbers(self):
        """Method to calculate how many even numbers are in the list"""
        count = 0
        for element in self.arr:
            if element % 2 == 0:
                count += 1
            else:
                continue
        return count

    def number_of_odd_numbers(self):
        """Method to calculate how many odd numbers are in the list"""
        count = 0
        for element in self.arr:
            if not element % 2 == 0:
                count += 1
            continue
        return count

    def __str__(self):
        return f'struc: {self.arr}'


class Objects:
    def __init__(self):
        self.db = PurePath(BASE_DIR, 'db', 'db.json')

    def load_file(self):
        with open(self.db) as file:
            return json.load(file)

    def get_person(self, **kwargs):
        data_base = self.load_file()
        if not kwargs:
            return data_base
        else:
            if 'id' in kwargs:
                for person in data_base:
                    if kwargs['id'] == person['id']:
                        return person
            else:
                raise ValueError('You must provide an id')

    def delete_person(self, id):
        data_base = self.load_file()
        for person in data_base:
            if person['id'] == id:
                data_base.remove(person)
        with open(self.db, 'w') as file:
            json.dump(data_base, file, indent=4)
        return f'Person with id {id}  was removed'


class Person(Objects):
    def __init__(self, names, last_name, age, email):
        super().__init__()
        self.names = names
        self.last_name = last_name
        self.age = age
        self.email = email

    def load_file(self):
        with open(self.db) as file:
            return json.load(file)

    def save(self):
        data_base = self.load_file()
        data = {
            'id': time.time(),
            'names': self.names,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email
        }
        data_base.append(data)
        with open(self.db, 'w') as file:
            json.dump(data_base, file, indent=4)
        return data

    def update(self, id):
        data_base = self.load_file()
        data = {
            'id': id,
            'names': self.names,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email
        }
        for person in data_base:
            if person['id'] == id:
                index = data_base.index(person)
                data_base[index] = data
        with open(self.db, 'w') as file:
            json.dump(data_base, file, indent=4)
        return data
