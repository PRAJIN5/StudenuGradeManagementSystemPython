class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.grades:
            self.grades.remove(grade)
        else:
            print("Grade not found.")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}, Average: {self.calculate_average()}")


class GradeManagementSystem:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def add_student(self, name):
        student = Student(self.next_id, name)
        self.students[self.next_id] = student
        print(f"Student {name} added with ID {self.next_id}.")
        self.next_id += 1

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed.")
        else:
            print("Student not found.")

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(grade)
            print(f"Grade {grade} added for student with ID {student_id}.")
        else:
            print("Student not found.")

    def update_grade(self, student_id, old_grade, new_grade):
        if student_id in self.students:
            self.students[student_id].remove_grade(old_grade)
            self.students[student_id].add_grade(new_grade)
            print(f"Grade updated for student with ID {student_id}.")
        else:
            print("Student not found.")

    def calculate_average_grade(self, student_id):
        if student_id in self.students:
            average = self.students[student_id].calculate_average()
            print(f"Average grade for student {student_id} is {average}.")
        else:
            print("Student not found.")

    def display_student(self, student_id):
        if student_id in self.students:
            self.students[student_id].display()
        else:
            print("Student not found.")

    def display_all_students(self):
        for student in self.students.values():
            student.display()

    def display_top_students(self, n):
        top_students = sorted(self.students.values(), key=lambda s: s.calculate_average(), reverse=True)[:n]
        for student in top_students:
            student.display()

    def calculate_overall_average_grade(self):
        total_grades = []
        for student in self.students.values():
            total_grades.extend(student.grades)
        if total_grades:
            overall_average = sum(total_grades) / len(total_grades)
            print(f"Overall average grade: {overall_average}.")
        else:
            print("No grades available.")


def menu():
    gms = GradeManagementSystem()

    while True:
        print("\n1. Add Student\n2. Remove Student\n3. Add Grade\n4. Update Grade\n5. Calculate Average Grade")
        print("6. Display Student\n7. Display All Students\n8. Display Top Students\n9. Calculate Overall Average Grade\n10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            gms.add_student(name)
        elif choice == '2':
            student_id = int(input("Enter student ID to remove: "))
            gms.remove_student(student_id)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            grade = float(input("Enter grade (0-100): "))
            gms.add_grade(student_id, grade)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            old_grade = float(input("Enter old grade (0-100): "))
            new_grade = float(input("Enter new grade (0-100): "))
            gms.update_grade(student_id, old_grade, new_grade)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            gms.calculate_average_grade(student_id)
        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            gms.display_student(student_id)
        elif choice == '7':
            gms.display_all_students()
        elif choice == '8':
            n = int(input("Enter the number of top students to display: "))
            gms.display_top_students(n)
        elif choice == '9':
            gms.calculate_overall_average_grade()
        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
