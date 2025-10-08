#

    #oop with file handling
import json

class student:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

        @classmethod
        def from_dict(cls, data):
            return cls(data['name'], data['age'], data['student_class'])
        
        def save_to_file(self, filename):
            with open(filename, 'w') as f:
                json.dump(self.__dict__, f)

 




               

              
    





      
    