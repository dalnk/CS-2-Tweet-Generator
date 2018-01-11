print("hello world")

x = None
x = "obj-c sucks"

print(type(x))

if x == "obj-c sucks":
    print("aloha")
elif x == None:
    print("str")
else:
    print("nothing worked")

some_list = [1,2,3,4,5, True, "Dennis", False]

for x in some_list:
    print(x)

for x in range(1, 100, 5):
    print(x)
x = 0
while x != 10:
    x += 1
    print(x)

some_list_comprehension = [x for x in range(100)]

for x in some_list_comprehension:
    print(x)

