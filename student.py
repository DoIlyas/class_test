# danh sách sinh viên

class student:

    # danh sách thuộc tính:
    id = ''
    name = ''

    # phương thức thêm sinh viên
    def add(self, id, name):
        print('Hàm add')
        self.id = id
        self.name = name

    # phương thức xoá sinh viên
    def remove(self, id):
        print('Hàm xoá')

    # phương thức sửa sinh viên
    def edit(self, id, name):
        print('Hàm sửa')

    # phương thức hiển thị thông tin sinh viên
    def show(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')


s = student()
s.add('01', 'Phạm Minh Dương')
s.show()
s.edit('10', 'Pham Minh Duong')
s.show()

s1 = student()
s1.add('02', 'Cao Văn Trinh')
s1.show()

s2 = student()
s2.add('03', 'Ngô Quang Huy')
s2.show()