# Lesson on while
print("\nLesson on while".upper())


count = 1
while count <= 4:
    print("loop")
    count += 1

number = 1
while number <= 10:
    if number % 8 == 0:
        break
    print(f"count odd numbers:{number}.")
    number += 1
