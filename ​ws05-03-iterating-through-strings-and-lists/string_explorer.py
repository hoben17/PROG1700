student_name = "Taylor Smith"

print("Student:", student_name)
print("Length:", len(student_name))

print("\nCharacters:")

for character in student_name:
    print(character)
print("\nCharacter positions:")
for index in range(len(student_name)):
    print(index, student_name[index])