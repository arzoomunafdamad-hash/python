classmates = ["Aaliyah", "Lakshmi", "Habibah", "Aashika", "Evana"]
print("Classmates List:", classmates)
print("total number of classmates:", len(classmates))

print("First classmate:", classmates[0])
print("Last classmate:", classmates[-1])
print("First three classmates:", classmates[:3])

classmates.append("Raina")
print("\nUpdated Classmates List after adding Raina:", classmates)
classmates.remove("Evana")
print("Updated Classmates List after removing Evana:", classmates)
classmates.sort()
print("Sort alphabetically:", classmates)
classmates.reverse()
print("Reverse:", classmates)



teacher = {"name": "Mrs. Asna", "subject": "SST", "experience": 7}
print("\nTeacher profile:", teacher)
print("Subject taught by the teacher:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not available"))
teacher["experience"] = 8
teacher["e mail"] = "mrs.asna@school.com"
teacher.pop("subject")
print("Updated Teacher profile:", teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Aaliyah", "Lakshmi", "Habibah", "Aashika", "Evana"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("student with roll number 3:", student_directory[3])