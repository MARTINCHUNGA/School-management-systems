from Person import Person
from Course import Course
 
class Trainer(Person) :
    
    def __init__(self, firstName, lastName, phoneNumber, dateOfBirth, address,id,domain,salary,gotRaise):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth, address)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = []
        self.gotRaise = False
        
    
    def checkForRaise(self):
        if len(self.courses) <= 4 and not self.gotRaise :
            self.salary += 1000
            self.gotRaise = True
        
    
    def addCourse(self,course) :
        if not isinstance(course,Course):
            pass
        
        else :
            self.courses.append(course)
        
    
    def convert_course_to_string(self) :
        if len(self.courses) != 0 :
            str_courses = ''
            count = 0
            for course in self.courses :
                str_ = course.name + ' ' + course.code + ';'
                str_courses += str_
                count += 1
                
                return str_courses 