vi_du_list = [1, 2, 3.14, 'vuminhdung.com', 'google.com']

print(vi_du_list)

# Truy cập phần tử thứ 4
print(vi_du_list[3])
# Thay đổi giá trị của phần tử thứ 4
vi_du_list[3] = 'vuminhdung.com.vn'
print(vi_du_list)

# 'google.com' ở vị trí 5, cũng là vị trí cuối cùng danh sách
# 2 lệnh in dưới đây sẽ cho cùng một kết quả
print('\nVí dụ index âm')
print(vi_du_list[-1])
print(vi_du_list[4])

print('\nVí dụ list trong list')
list_trong_list = [[1, 2], [3, 4]]
print(list_trong_list[0])
print(list_trong_list[0][1])

print('\nVí dụ slice')
print(vi_du_list[1:4])

print('\nTrick với slice')
print(vi_du_list[2:])  # Từ thứ 2 đến cuối
print(vi_du_list[:3])  # Từ đầu đến thứ 2
print(vi_du_list[1:-2])  # Từ thứ 1 đến thứ 2 từ cuối
print(vi_du_list[:])  # Lấy tất cả

print('\nHàm len()')
print(len(vi_du_list))

print('\nToán tử và list')
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)

print('\nVí dụ del')
c = [6, 9, 69]
print(c)
del c[2]
print(c)
del c
print(c)
