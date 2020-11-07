variable = 96


def function():
    global variable  # (1)
    variable = 69


function()
print(variable)
