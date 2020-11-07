# Ví dụ biến toàn cục
# Biến này được gán ngoài hàm nên có global scope
global_variable = 10


# Ví dụ biến cục bộ
def a_useless_function():
    # Biến này được gán trong thân hàm nên có local scope
    local_variable = 10
