global_variable = 69


def function():
    # Hiện đang ở local scope của function()
    # Vẫn có thể truy cập được biến `global_variable` từ global scope
    print(global_variable)


function()
