class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.graduated = False

class Faculty:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            student.graduated = True
            self.students.remove(student)
            class StudyField(enumerate):
                MECHANICAL_ENGINEERING = "Mechanical Engineering"
                SOFTWARE_ENGINEERING = "Software Engineering"
                FOOD_TECHNOLOGY = "Food Technology"
                URBANISM_ARCHITECTURE = "Urbanism and Architecture"
                VETERINARY_MEDICINE = "Veterinary Medicine"

class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, field):
        new_faculty = Faculty(name, field)
        self.faculties.append(new_faculty)
        return new_faculty

    def get_faculty_by_student_id(self, student_id):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.student_id == student_id:
                    return faculty
        return None

    def display_all_faculties(self):
        print("University Faculties:")
        for faculty in self.faculties:
            print(f"{faculty.name} - Field: {faculty.field}")

    def display_students_by_faculty(self, faculty):
        print(f"Current Enrolled Students in {faculty.name} Faculty:")
        for student in faculty.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

    def display_graduates_by_faculty(self, faculty):
        print(f"Graduates from {faculty.name} Faculty:")
        for student in faculty.students:
            if student.graduated:
                print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

def main():
    university = University()

    while True:
        print("\nUniversity Management System")
        print("1. Enroll Student")
        print("2. Graduate Student")
        print("3. Display Enrolled Students")
        print("4. Display Graduates")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")

            faculty_name = input("Enter faculty name to enroll the student: ")
            field = input("Enter field of the faculty: ")

            faculty = next((f for f in university.faculties if f.name == faculty_name and f.field == field), None)
            if not faculty:
                faculty = university.create_faculty(faculty_name, field)

            student = Student(student_id, name, email)
            faculty.enroll_student(student)
            print(f"Student {name} enrolled in {faculty_name} Faculty.")

        elif choice == '2':
            student_id = input("Enter student ID to graduate: ")
            faculty = university.get_faculty_by_student_id(student_id)
            if faculty:
                student = next((s for s in faculty.students if s.student_id == student_id), None)
                if student:
                    faculty.graduate_student(student)
                    print(f"Student {student.name} graduated from {faculty.name} Faculty.")
                else:
                    print(f"Student with ID {student_id} not found in {faculty.name} Faculty.")
            else:
                print(f"Student with ID {student_id} not found in any Faculty.")

        elif choice == '3':
            faculty_name = input("Enter faculty name to display students: ")
            field = input("Enter field of the faculty: ")

            faculty = next((f for f in university.faculties if f.name == faculty_name and f.field == field), None)
            if faculty:
                university.display_students_by_faculty(faculty)
            else:
                print(f"Faculty {faculty_name} in {field} Field not found.")

        elif choice == '4':
            faculty_name = input("Enter faculty name to display graduates: ")
            field = input("Enter field of the faculty: ")

            faculty = next((f for f in university.faculties if f.name == faculty_name and f.field == field), None)
            if faculty:
                university.display_graduates_by_faculty(faculty)
            else:
                print(f"Faculty {faculty_name} in {field} Field not found.")

        elif choice == '5':
            print("Exiting University Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
1
