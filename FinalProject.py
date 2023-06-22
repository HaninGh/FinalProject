"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Hanin Kamal Ghannam
Delivery Date : 22-06-2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)

import uuid
class Course:

    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

    def __repr__(self):
        return f"Course(course_id={self.course_id}, course_name='{self.course_name}', course_mark={self.course_mark})"

course = Course("Python Programming", 100)
print(course)

 #TODO 3 define static variable indicates total student count
class Student :
        #define static variable indicates total student count
        total_student_count = 0
        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
            Student.total_student_count += 1
        def __repr__(self):
            return f"Student(name='{self.name}', student_id={self.student_id})"

student1 = Student("Hanin Gh", 12345)
student2 = Student("Hamza Gh", 67890)
print(Student.total_student_count)

#TODO 4 define a constructor which includes
def __init__(self, student_name, student_age, student_number, courses_list):
    self.student_id = uuid.uuid4()
    self.student_name = student_name
    self.student_age = student_age
    self.student_number = student_number
    self.courses_list = courses_list
    Student.total_student_count += 1
def __repr__(self):
    return f"Student(student_id={self.student_id}, student_name='{self.student_name}', student_age={self.student_age}, student_number={self.student_number}, courses_list={self.courses_list})"
    student_name = input("Enter the student name: ")
    student_age = int(input("Enter the student age: "))
    student_number = input("Enter the student number: ")
    courses_list = [Course("Python Programming", 100), Course("Data Structures", 75)]

    student = Student(student_name, student_age, student_number, courses_list)
    print(student)

# TODO 5 define a method to enroll new course to student courses list
def enroll_new_course(self, course):
    """
    Enrolls a new course to the student's courses list.

    Args:
        course (Course): The course to enroll.

    Returns:  
        None.
    """
    
    self.courses_list.append(course)
def get_student_details(self):
     """
     Returns the student details as a dictionary.

     Returns:
         dict: The student details.
     """

     return self.__dict__
def get_student_courses(self):
    """
    Returns the student's courses list.

    Returns:
        list: The student's courses list.
    """

    return self.courses_list

#TODO 6 print student courses with their marks
def print_student_courses_with_marks(self):
    """
    Prints the student's courses with their marks.

    Returns:
        None.
    """

    print("Course name: Mark")
    for course in self.courses_list:
        if course is not None:
            print(f"{course.course_name}: {course.course_mark}")

    if len(self.courses_list) == 0:
        print("No courses enrolled yet.")

# method to get student_average as a value
#TODO 7 return the student average
def get_student_average(self):
        """
        Gets the student's average mark.

        Returns:
            float: The student's average mark.
        """

        total_marks = 0
        number_of_courses = len(self.courses_list)

        for course in self.courses_list:
            if course is not None:
                total_marks += course.course_mark

        student_average = total_marks / number_of_courses

        return student_average

# in Global Scope
# TODO 8 declare empty students list
students = []

while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))
while True:

    try:
        selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))
    except ValueError:
        print("Please enter a valid selection.")
        continue

    if selection == 1:
        # code to add a new student
        break
    elif selection == 2:
        # code to delete a student
        break
    elif selection == 3:
        # code to display a student
        break
    elif selection == 4:
        # code to get a student's average
        break
    elif selection == 5:
        # code to add a course to a student
        break
    elif selection == 6:
        break
    else:
        print("Please enter a valid selection.")

        # TODO 10 make sure that Student number is not exists before

    if selection == 1:
    
        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")
    
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")
    
def add_student(student_number, student_name, student_age):

    for student in students:

        if student.student_number == student_number:
            print("Student number already exists.")
            return

    student = Student(student_name, student_age, student_number)
    students.append(student)


        # TODO 11 create student object and append it to students list

        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 16 call a function to exit the program
        pass