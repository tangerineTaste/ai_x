from django.db import models

class Student(models.Model): # 앱명_클래스명(student_student)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True) 
    major = models.CharField(max_length=100, null=True) # 기본이 null=False 
    age = models.IntegerField(default=0) 
    grade = models.IntegerField(default=1) 
    def __str__(self): 
        return "{}:{}({}, {}세 {}학년)".format(self.id, self.name, self.major, self.age, self.grade)