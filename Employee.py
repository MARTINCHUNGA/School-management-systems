
from Person import Person
from datetime import datetime
from Enrollment import enrollment

class Employee(Person) :
    
    def __init__(self, firstName, lastName, phoneNumber, dateOfBirth, address,id,title,dateOfEmployment):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth, address)
        self.id = id
        self.title = title
        self.international = False
        self.dateOfEmployment = dateOfEmployment
        self.enrolled = []
        
        
    def addEnrollment(self,enroll):
        if not isinstance(enroll,enrollment) :
            #Some code here
            pass
        else :
            self.enrolled.append(enroll)
        
        
    
    
    def isPartTime(self):
        return False
        
    
    def isOnProbation(self) :
        len(self.enrolled) <= 3
        