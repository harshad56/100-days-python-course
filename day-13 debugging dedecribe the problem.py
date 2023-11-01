# this function is not execute

def my_function():
    for i in range(1, 20):  # range 1 to 19
        if i == 20:
            # this statement is not run, because range function is execute  1 to 19 not 20
            print("you got it")


my_function()
# --------------------------------------------------------------------------

# this function is execute


def my_function():
    for i in range(1, 21):  # range is 1 to 20
        if i == 20:
            # this execute because range is between 1 to 21 so 20 is lise between 1 to 21
            print("you got it")


my_function()
