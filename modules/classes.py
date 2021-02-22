import names
import random
import string
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        tmp_avg_grade = 0
        for element in self.data_sheet.courses:
            tmp_avg_grade += int(element.grade)
        avg_grade = tmp_avg_grade/len(self.data_sheet.courses)
        return avg_grade
        

        
class DataSheet:
    def __init__(self, courses = []):
        self.courses = courses

    def get_grades_as_list(self):
        gradelist = []
        for element in self.courses:
            gradelist.append(element.grade)
        return gradelist

class Course:
    def __init__(self, name, classroom, teacher, ECTS, grade = 0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade



def generate_students(number):
    course_names = ["Secruity", "Typescript", "Kotlin"]
    genders = ["male", "female"]
    grades = ["-3", "00", "02", "4", "7", "10", "12"]

    for x in range(0, number):
        with open("week3.csv", "a") as file_obj:
            name = names.get_full_name()
            image_url = ''.join(random.choice(string.ascii_lowercase)for i in range(15))
            course = Course(random.choice(course_names),'D klassen', 'Thomas', '20', random.choice(grades))
            data_sheet = DataSheet([course])
            student = Student(name, random.choice(genders), data_sheet, image_url)
            text_to_file = "name: {stud_name}, course name: {course_name}, teacher: {teacher}, ECTS: {ECTS}, classroom: {classroom}, grade: {grade}, image_url: {image_url}, gender: {stud_gender}" .format(
                stud_name=student.name, course_name=course.name, teacher=course.teacher, ECTS=course.ECTS, classroom=course.classroom, grade=course.grade, image_url=student.image_url, stud_gender=student.gender)
            file_obj.write(text_to_file + "\n")


def read_students_to_list():
    student_list = []
    with open("week3.csv", "r") as file_obj:
        lines = file_obj.readlines()
        for line in lines:
          name = (line.split("name: "))[1].split(",")[0]
          course_name = (line.split("course name: "))[1].split(",")[0]
          teacher = (line.split("teacher: "))[1].split(",")[0]
          ECTS = (line.split("ECTS: "))[1].split(",")[0]
          classroom = (line.split("classroom: "))[1].split(",")[0]
          grade = (line.split("grade: "))[1].split(",")[0]
          image_url = (line.split("image_url: "))[1].split(",")[0]
          gender = (line.split("gender: "))[1].split(",")[0]
          course = Course(course_name, classroom, teacher, ECTS, grade)
          data_sheet = DataSheet([course])
          student = Student(name, gender, data_sheet, image_url)
          student_list.append(student)
    return student_list

def sorted_list():
    student_list = read_students_to_list()
    new_list = sorted(student_list, key=lambda x: x.get_avg_grade(), reverse=True)
    return new_list

def plot_students(students):

    for student in students:
        plt.bar([student.name],[student.get_avg_grade()],width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

