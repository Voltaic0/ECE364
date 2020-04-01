#! /usr/local/bin/python3.7

##############################
# Lecture 7: OOP
##############################

"""
References:

* Python documentations:
    - Classes:                      https://docs.python.org/3.7/tutorial/classes.html
    - Data Model:                   https://docs.python.org/3.7/reference/datamodel.html
* Books:
    - Beginning Python              https://www.apress.com/us/book/9781484200292
        Chapter 7: More Abstraction:

    - Python Recipes Handbook       https://www.apress.com/us/book/9781484202425
        Chapter 7: Classes and Objects

    - Pro Python                    https://www.apress.com/us/book/9781430227571
        Chapter 4: Classes

* Websites:
    - Real Python:                  https://realpython.com/python3-object-oriented-programming/
    - The Python Guru               https://thepythonguru.com/python-operator-overloading/
"""


class Course:

    def __init__(self, name, dept="ECE", number="101", hours=3, isGradLevel=False):
        self.CourseName = name
        self.Number = number

        self._validateCreditHours(hours)
        self.CreditHours = hours

        self.IsGraduateLevel = isGradLevel

        self._validDepartments = ["ECE", "ME", "ENM", "MATH"]
        self._validateDepartment(dept)
        self.Department = dept

    def __str__(self):
        return (f"{self.Department}{self.Number} {self.CourseName},"
                f" ({self.CreditHours} Credit Hour(s))")

    def _validateDepartment(self, department):
        """
        Validates the department string to be one of the acceptable ones.
        """
        if department not in self._validDepartments:
            raise ValueError("Department entered is not valid.")
        self.Department = department

    def _validateCreditHours(self, creditHours):
        """
        Validates the credit hours to be between 1 & 4.
        """
        if creditHours < 1 or creditHours > 4:
            raise ValueError("Credit hours must be between 1 and 4.")

        self.CreditHours = creditHours


class Student:

    def __init__(self, firstName, lastName):

        self.firstName = firstName
        self.lastName = lastName
        self.courses = []

    def __str__(self):
        # This special function creates a "human-readable" string representation.
        return f"{self.firstName} {self.lastName}"

    def __repr__(self):
        # This special function creates a unique unambiguous instance string representation
        # for debugging purposes.
        return f"{self.firstName} {self.lastName}"

    def getInfo(self):
        """
        Returns a properly formatted string of the name and the course work.
        """
        strCourses = [str(c) for c in self.courses]
        courses = "Registered in:\n{0}.".format(",\n".join(strCourses)) if self.courses else "Unregistered."

        about = f"Student name is {self.lastName}, {self.firstName}."

        return about + "\n" + courses

    def __add__(self, course):

        self.addCourse(course)
        return self

    def addCourse(self, someCourse):
        self.courses.append(someCourse)


# ###############################################################################
# Inheritance: Extending Classes, (subclassing)
# ###############################################################################


class GraduateStudent(Student):
    """
    A Class that holds some information about graduate students.
    This is referred to as a "Child Class", or a "Subclass"
    """
    def __init__(self, firstName, lastName, degree="Ph.D."):
        self.IsGraduate = True
        self.Degree = degree

        super().__init__(firstName, lastName)

    def __str__(self):
        return f"{self.firstName} {self.lastName}, ({self.Degree} Candidate)"

    def addCourse(self, someCourse):

        if not someCourse.IsGraduateLevel:
            raise ValueError("Cannot add a non-graduate level course.")

        self.courses.append(someCourse)

    # Function Overloading
    # ####################################
    def addCourses(self, *args):

        for course in args:
            if not course.IsGraduateLevel:
                raise ValueError("Cannot add a non-graduate level course.")

            self.courses.append(course)

    def doSomething(self, **kwargs):
        print("The Type of the input argument 'kwargs' is " + str(type(kwargs)))

        for k, v in kwargs.items():
            print(f"key: {k}, value: {v}")


if __name__ == "__main__":

    course1 = Course("Intro to Engineering")
    print(course1)
    print()

    course2 = Course("Advanced Math for Engineers", "MATH", "303")
    print(course2)
    print()

    student = Student("Mary", "Smith")

    print(student)
    print(student.getInfo())
    print()
    print()

    student.addCourse(course1)

    student + course2

    print(student)
    print(student.getInfo())
    print()
    print()

    gradStudent = GraduateStudent("Scooby", "Doo")
    print(gradStudent)
    print(gradStudent.getInfo())
    print()
    print()

    gradCourse1 = Course("Introduction to A.I.", "ECE", "565", 3, True)
    gradCourse2 = Course("Computer Vision", "ECE", "661", 3, True)

    # # This will raise an error
    # gradStudent += course2

    gradStudent += gradCourse1
    print(gradStudent)
    print(gradStudent.getInfo())
    print()
    print()

    # Via overloaded function:
    gradStudent.addCourses(gradCourse1, gradCourse2)
    print(gradStudent.getInfo())

    gradStudent.doSomething(isSenior=True, dancingStyle="Tango", age=32)
    gradStudent.doSomething(Today="Monday", Effort="Maximum", Percerntage=100.0)


