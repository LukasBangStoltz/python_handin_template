class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        tmp_avg_grade = 0
        for element in self.data_sheet.courses:
            tmp_avg_grade += element.grade
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
    def __init__(self, name, classroom, teacher, ETCS, grade = 0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade



def print_shit():
    print("shit")