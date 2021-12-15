class Student:
    
    def __init__(self, name = '', ID = 0, major ='', gpa= 0, creditsTaken = 0.0) -> None:
        self.name = name
        self.ID = ID
        self.major = major
        self.gpa = gpa
        self.creditsTaken = creditsTaken
        
    def setName(self, name):
        self.name = name
    
    def setID(self, ID):
        self.ID = ID
    
    def setMajor(self, major):
        self.major = major
    
    def setGpa(self, gpa):
        self.gpa = gpa
    
    def seCreditsTaken(self, creditsTaken):
        self.creditsTaken = creditsTaken
    
    def getName(self) -> str:
        return self.name
    
    def getID(self) -> int:
        return self.ID

    def getMajor(self) -> str:
        return self.major
    
    def getGpa(self) -> float:
        return self.gpa
    
    def getcreditsTaken(self) -> int:
        return self.creditsTaken
    
    def calculateGpa(self, tClassGrade, credits ) -> float:
        
        points = {'A' : 4.00, "B" : 3.00, 'C' : 2.00, 'D' : 1.00, 'F' : 0.00}
        
        oldCreditsCount = self.creditsTaken
        self.creditsTaken += credits
        
        newGpa = ((self.getGpa()*oldCreditsCount) + credits * points.get(tClassGrade))/(self.creditsTaken + oldCreditsCount)
        
        self.gpa = newGpa
        
        return self.gpa
        
        
    def __str__(self) -> str:
        text = f'''\tStudent Id : {self.ID}
        Student Name : {self.name}
        Student Major : {self.major}
        Student GPA : {self.gpa}
        '''
        return text
    
    
std = Student('Ahmad Nasser', 202105339, 'Computer Science', 3.00)

print(std)

std.calculateGpa('A', 3)

print(std)