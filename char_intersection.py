name = str(input("first name?: "))
name2 = str(input("second name?: "))

#intersection
set_1 = {name}
set_2 = {name2}
set_3 = set_1.intersection(set_2)

print(set_3)