# sử dụng thuộc tính của lớp cha
class Xe:
    name = 'Đây là tên xe'

class XeDap(Xe):
    def show_name(self):
        print(self.name)

x = XeDap()
x.show_name()


# sử dụng phương thức của lớp cha
class Xe:
    def set_name(self, name):
        self.name = name

class Xedap(Xe):
    def show_name(self):
        # sử dụng phương thức của lớp cha
        self.set_name("Xe đạp")

        # sử dụng thuộc tính của lớp cha
        print(self.name)

x = Xedap()
x.show_name()
