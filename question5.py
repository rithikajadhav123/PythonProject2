import json

student = {
    "name": "Rithika",
    "register_number": "24BEIS123",
    "course": "BE Information Science",
    "marks": 85
}

json_string = json.dumps(student)

print("JSON String:")
print(json_string)

python_dictionary = json.loads(json_string)

print("\nPython Dictionary:")
print(python_dictionary)