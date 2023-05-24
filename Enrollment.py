from datetime import datetime
from Employee import Employee
from Course import Course

class Enrollment :
    
    def __init__(self,employee,course):
        if not isinstance(employee,Employee) :
            pass
        if not isinstance(course,Course) :
            pass
            
        self.employee = employee
        self.course = course
        self.grade = None
        self.date = datetime.now()
        
    def setGrade(self,grade):
         self.grade = grade
    
    def __repr__(self):
        return f"Enrolment: {self.employee.firstName} {self.employee.lastName} - {self.course.code}: {self.course.trainers}"
        