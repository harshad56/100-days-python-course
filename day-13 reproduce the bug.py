# error getting code

from random import randint

disc_img = ["1", "2", "3", "4", "5", "6"]
# list index  0    1     2   3    4    5

# so it get error because position is limtied 0 to 5th index ,6th position is not available
disc_num = randint(1, 6)

print(disc_img[disc_num])

# ------------------------------------------------------------------------------
# fixed code

disc_img = ["1", "2", "3", "4", "5", "6"]
# list index  0    1     2   3    4    5

# so it execute because position is limtied 0 to 5th index
disc_num = randint(1, 5)

print(disc_img[disc_num])
