"""name = str(input("first name?: "))
name2 = str(input("second name?: "))"""




name = set(input())
name2 = set(input())

#intersection


set3 = (name.intersection(name2))  #u need to make the intersection a string

set3 = "".join(set3)

print(set3)


