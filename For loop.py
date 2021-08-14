# Lesson on for
print("\nLesson on for".upper())

colours = ['blue', 'green', 'red', 'purple']
for colour in colours:
    print(colour)

for colour in colours:
    if colour == 'blue':  # continue with blue but not print blue
        continue
    elif colour == 'red':  # goes from blue green red, stop at red
        break
    print(colour)  # only prints green as red is stopped

point1 = (5.5, 6.3, 9.6)