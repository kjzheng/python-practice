xmen_file = open('xmen_base.txt', 'r')
print(xmen_file.read())  # print out whats in the txt file
print(xmen_file.seek(20))
print(xmen_file.close())  # close the txt files next line of rad cant read
"""
xmen_file wont work after this
"""
print(xmen_file.read())