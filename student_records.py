# student_records_clean.py
# Internship Task 7: Dictionaries & JSON Handling

import json

# 1. Dictionary of student details
student_data = {
    "ST01": {"name": "Rohit", "age": 22, "grades": [85, 90, 88]},
    "ST02": {"name": "Anika", "age": 20, "grades": [92, 81, 79]},
    "ST03": {"name": "Meera", "age": 21, "grades": [75, 84, 91]}
}

# 2. Original records
print("Original Records:")
for sid, info in student_data.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 3. Update & delete
student_data["ST02"]["age"] = 21
del student_data["ST03"]

print("\nAfter Update/Delete:")
for sid, info in student_data.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 4. Loop through dictionary
print("\nLooping Records:")
for sid, info in student_data.items():
    print(f"{sid} -> Name: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 5. Convert dictionary to JSON string (compact)
student_json = json.dumps(student_data, indent=2)
print("\nJSON Format:")
print(student_json)

# 6. Save JSON to file
with open("student_data_clean.json", "w") as f:
    json.dump(student_data, f, indent=2)

# 7. Load JSON back
with open("student_data_clean.json", "r") as f:
    loaded_data = json.load(f)

print("\nLoaded from JSON:")
for sid, info in loaded_data.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")