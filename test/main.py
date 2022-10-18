def index_data():
    """Hàm nhập dữ liệu vào mảng"""
    global listStudents
    while True:
        print("Nhập tên sinh viên cần thêm: ")
        tmp = input()
        if tmp == '0':
            break
        listStudents.append(tmp)

def find_student(name, listStudents):
    """Hàm tìm thông tin sinh viên"""
    result = -1
    for i in range(0, len(listStudents)):
        if listStudents[i] == name:
            result = i
            break

    return result

#Chương trình chính
print("Chương trình quản lý sinh viên bằng python")

print("Bước 1: nhập danh sách sinh viên")
print("Gõ 0 để thoát khỏi chương trình")

listStudents = []
index_data()
while True:
    print("Bước 2: Nhập tên sinh viên muốn tìm")
    name = input()
    if name == '0':
        break

    index = find_student(name, listStudents)

    if(index == -1):
        print("Không tìm thấy sinh viên")
    else:
        print("Sinh viên được tìm thấy tại vị trí ", index+1)
    if(name == 'Dương Thị Thái Hà'):
        print("Tớ yêu cậu rất nhiều")
