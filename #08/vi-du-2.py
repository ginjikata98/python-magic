def function_1():
    local_variable_1 = 69
    print(local_variable_1)

    # Hiện đang ở local scope của function_1()
    # Do đó không thể truy cập biến từ local_scope của function_2()
    print(local_variable_2)


def function_2():
    local_variable_2 = 96


function_1()
