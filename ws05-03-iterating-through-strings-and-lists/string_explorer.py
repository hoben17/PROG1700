student_name = "Alexander"

print("Student", student_name)
print("Lenght:", len(student_name))

print("\nCharacters")


for character in student_name:
    print(character)
    print("\nCharacter")

    for index in range(len(student_name)):
        print(index, student_name[index])