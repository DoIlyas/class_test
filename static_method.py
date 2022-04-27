# class Mathematics:
#     def add_number(self, x, y):
#         return x + y
#
# m = Mathematics()
# print(m.add_number(11, 15))


# sử dụng phương thức tĩnh
class Mathematics:
    @staticmethod    # thêm cái này để sử dụng phương thức tĩnh
    def add_numbers(x ,y):   # vì static không khởi tạo đối tượng nên không có tham số self
        return x + y

# có thể được gọi mà ko cần khởi tạo class
# cú pháp: class_name.method_name()
print(Mathematics.add_numbers(11, 17))