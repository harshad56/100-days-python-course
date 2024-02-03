target = int(input(
    "write a number you want calculate the sum of  even nobetween them to write even number upto:"))

even_no = 0

for i in range(0, target+1, 2):
    even_no += i

print(even_no)

# alternative option

# option = 0
# for i in range(1, target+1):
#     if i % 2 == 0:
#         option += i
# print(option)
