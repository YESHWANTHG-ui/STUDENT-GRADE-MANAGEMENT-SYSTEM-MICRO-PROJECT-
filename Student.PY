"""Simple Student Grade Management System."""


def add_student(students):
    student_id = input('Enter student ID: ').strip()
    if student_id == '':
        print('Student ID cannot be empty.')
        return
    if student_id in students:
        print('Student already exists.')
        return

    name = input('Enter student name: ').strip()
    if name == '':
        print('Student name cannot be empty.')
        return

    students[student_id] = {'name': name, 'grades': []}
    print('Student added successfully.')


def add_grade(students):
    student_id = input('Enter student ID: ').strip()
    if student_id not in students:
        print('Student not found.')
        return

    grade = input('Enter grade letter (A/B/C/D/F): ').strip().upper()
    if grade not in ('A', 'B', 'C', 'D', 'F'):
        print('Invalid grade letter.')
        return

    students[student_id]['grades'].append(grade)
    print('Grade added successfully.')


def view_student(students):
    student_id = input('Enter student ID: ').strip()
    if student_id not in students:
        print('Student not found.')
        return

    student =3 students[student_id]
    print('ID:', student_id)
    print('Name:', student['name'])
    print('Grades:', student['grades'])
    if student['grades']:
        print('Total grades:', len(student['grades']))
    else:
        print('No grades yet.')


def list_students(students):
    if not students:
        print('No students available.')
        return

    for student_id, student in students.items():
        print('ID:', student_id)
        print('Name:', student['name'])
        print('Grades:', student['grades'])
        if student['grades']:
            average = sum(student['grades']) / len(student['grades'])
            print('Average:', round(average, 2))
            print('Average letter:', get_grade_letter(round(average)))
        else:
            print('Average: N/A')
        print('-' * 20)


def menu():
    print('\nStudent Grade Management System')
    print('1. Add student')
    print('2. Add grade')
    print('3. View student')
    print('4. List students')
    print('5. Exit')


def main():
    students = {}

    while True:
        menu()
        choice = input('Choose an option: ').strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            add_grade(students)
        elif choice == '3':
            view_student(students)
        elif choice == '4':
            list_students(students)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()
