from Trainer import Trainer
from Enrollment import Enrollment
class Course :
    
    def __init__(self,id,name,code,maximum,minimum) :
        self.id = id
        self.name = name
        self.code = code
        self.maximum = maximum
        self.minimum = minimum
        self.trainers = []
        self.enrollments = []
        
    def __repr__(self) -> str:
        return f"Course : '{self.id} ': {self.name} - {self.code}"
        
    def addTrainer(self,trainer):
        if isinstance(trainer,Trainer):
            self.trainers.append(trainer)
        elif isinstance(trainer,list) :
            for entry in trainer :
                if not isinstance(trainer,Trainer) :
                    pass
            self.trainers = trainer
        else :
            pass
    
    def addEnrollment(self,enroll):
        if not isinstance(enroll,Enrollment):
            pass
        if len(self.enrollments) == self.maximum :
            pass
        self.enrollments.append(enroll)
    
    
    
    def isCancelled(self):
        return len(self.enrollments) < self.minimum
        