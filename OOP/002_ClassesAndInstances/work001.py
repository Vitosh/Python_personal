class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.ram = None

    def set_ram(self, ram):
        self.ram = ram

    def __str__(self):
        return f'{self.model}; {self.brand}; {self.ram }'

asus = Laptop('rog', 'Asus')
dell = Laptop('inspiron', 'Dell')
asus.ram = 16
print(asus.__dict__)
