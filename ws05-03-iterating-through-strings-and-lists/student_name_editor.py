student_name = " jordan smith "
print("Origional:", repr(student_name))
print("length:", len(student_name))
print("First character:", repr(student_name[0]))
student_name = student_name.strip()
student_name = student_name.title()

print("Cleaned:", student_name)
student_name = student_name.replace(" ", "")
print("Without Spaces:", student_name)