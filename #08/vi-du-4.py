variable = 'global variable'


def function():
    variable = 'local_variable'  # (1)
    print(variable)  # (2)


function()  # (3)
print(variable)  # (4)
