def function():
    # Một biến cục bộ
    local_variable = 10


# Hiện đang ở global scope nên không thể truy cập biến trong local scope của function()
print(local_variable)