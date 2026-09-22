file = open("student.txt", "w")

file.write("Name: Rithika\n")
file.write("Register Number: 24BEIS123\n")
file.write("Course: BE Information Science\n")
file.write("Marks: 85\n")

file.close()

file = open("student.txt", "r")

content = file.read()

print("Student Information:")
print(content)

file.close()
