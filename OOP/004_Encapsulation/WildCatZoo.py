class Lion:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Lion"

    def get_needs(self):
        return 50

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Tiger:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Tiger"

    def get_needs(self):
        return 45

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Cheetah"

    def get_needs(self):
        return 60

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Keeper:
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Keeper"

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Caretaker:
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Caretaker"

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Vet:
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Vet"

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Zoo:
    def __init__(self, name: str, budget, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__worker_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return f'Not enough space for worker'

    def fire_worker(self, worker):
        for w in self.workers:
            if worker == w.name:
                self.workers.remove(w)
                return f'{worker} fired successfully'
        return f'There is no {worker} in the zoo'

    def pay_workers(self):
        money_needed = sum([worker.salary for worker in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy.'

    def tend_animals(self):
        money_needed = sum([animal.get_needs() for animal in self.animals])

        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f'You have {len(self.animals)} animals\n'
        for animal_type in ("Lion", "Tiger", "Cheetah"):
            result += f'----- {len([animal for animal in self.animals if animal.type == animal_type])} {animal_type}s:\n'
            for a in [animal for animal in self.animals if animal.type == animal_type]:
                result += f'{repr(a)}\n'
        return result

    def workers_status(self):
        result = ""
        result += f'You have {len(self.workers)} workers\n'
        for worker_type in ("Keeper", "Caretaker", "Vet"):
            result += f'----- {len([worker for worker in self.workers if worker.type == worker_type])} {worker_type}s:\n'
            for w in [worker for worker in self.workers if worker.type == worker_type]:
                result += f'{repr(w)}\n'
        return result

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
