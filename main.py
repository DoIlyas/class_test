class Animal:
    # các thuộc tính:
    name = ''
    sex = ''

    def set_data(self, name, sex):
        self.name = name
        self.sex = sex

    def show(self):
        print(f'Name: {self.name}')
        print(f'Sex: {self.sex}')

    # các hành động:
    def eat(self):
        print('Ăn')
    def drink(self):
        print('Uống')
    def run(self):
        print('Chạy')

# Dog kế thừ từ Animal
class Dog(Animal):
    def bark(self):
        print('Con chó sủa gâu gâu gâu')

a = Animal()
a.set_data('Chó Nhật', 'Đực')
a.show()
d = Dog()
d.eat()
d.run()
d.bark()