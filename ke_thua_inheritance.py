# sử dụng thuộc tính của lớp cha
class Xe:
    name = 'Đây là tên xe'

class Xe_Dap(Xe):
    def show_name(self):
        print(self.name)

x = Xe_Dap()
x.show_name()


# sử dụng phương thức của lớp cha
class Xe:
    def set_name(self, name):
        self.name = name

class Xe_dap(Xe):
    def show_name(self):
        # sử dụng phương thức của lớp cha
        self.set_name("Xe đạp")

        # sử dụng thuộc tính của lớp cha
        print(self.name)

x = Xe_dap()
x.show_name()