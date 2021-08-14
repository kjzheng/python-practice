# Lesson on def,\n,\t,var
def test_1(test123):
    print(f'Type in ?+?, {test123}')


def test_2(test456):
    print(f"Good morning, {test456}")


a = 2.65/3
b = 3.68*3

if __name__ == '__main__':
    test_2("everyone!")
    test_2("everyone!")
    test_1(a ** 2 + b ** 9)

random_number = 5 % 3*6**4/4
print("\n\tTeStInG var+a+b.".lower(), "\n\tIt is", "\n\t", random_number+a+b, "\n\t'Trying out things in python'")
print(random_number == 648)

# Lesson on list
print("\nLesson on list".upper())
my_list = [1, 2, 3, 4, 5, 6, 'g', True, False]
print(my_list)
print(my_list[0:5:2])  # print from index 0 to 5 which is 1,2,3,4,5,6 but with jumps of 2 that shows 1,3,5
my_list.pop(5)
print("List had been popped of number 6. List is", my_list, ".")
my_list.insert(5, 6)
print("List had been added back with number 6. List is", my_list, ".")

# Lesson on tuple
print("\nLesson on tuple".upper())
my_tuple1 = (3.0, "A")
my_tuple2 = (4.0, "B")
print(my_tuple1+my_tuple2)  # tuple of 2+2
aa, bb, cc, dd = my_tuple1+my_tuple2  # set 2+2 into 4 things
print(aa, bb, cc)  # print only first 3 of a 4-set
print("The coordinates are (%s, %s) (%s, %s)." % (my_tuple1+my_tuple2))
print("The coordinates are (%s, %s) (%s, %s)." % (aa, bb, cc, dd))

# Lesson on dict
print("\nLesson on dict".upper())
class_ages = {'za': 30, 'zb': 29, 'zc': 32, 'zd': 45}
print(class_ages['zb'])
class_ages.pop('zc')
print(class_ages)
print(class_ages.keys())
print(class_ages.values())
print(class_ages.values(), class_ages.keys())  # set 2 to show in 1 line
print(list(class_ages.values()))  # change dict to list showing only values
print(list(class_ages.keys()))
weights = dict(za=30, zb=29, zd=45)
print(weights)
print(class_ages)
