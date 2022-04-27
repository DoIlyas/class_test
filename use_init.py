class Dog:
    name = ''
    country = ''

    def __init__(self, name, country):
        self.name = name
        self.country = country


d = Dog('Husky', 'England')
print(d.name)
print(d.country)