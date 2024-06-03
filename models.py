from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class hlo(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField(default=0)
    addr=models.CharField(max_length=50)
    email=models.EmailField(null=True, blank=True)

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.department
    
    # we order to store in sequence by a to z

    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=100, default=0)

    def __str__(self) ->str:
        return self.student_id
    
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
    

class Student(models.Model):
    # we use foreign key (one to many) as one dept can have many students
    department=models.ForeignKey(Department,related_name="depart" , on_delete=models.CASCADE)
    # we use onetoone relationship as one student will have only one id
    student_id=models.OneToOneField(StudentID, related_name="stdid", on_delete=models.SET_NULL, null=True)
    # student_id=models.OneToOneField(StudentID , related_name="studentid" , on_delete=models.SET_NULL, null=True)
    student_name=models.CharField(max_length=100)
    # repetation will not allow as unique=true
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self):
        return self.student_name
    


    class Meta:
        ordering=['student_name']
        # name we use
        verbose_name="student"

class SubjectMarks(models.Model):
        student=models.ForeignKey(Student ,related_name="studentmark", on_delete=models.CASCADE)
        subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
        marks=models.IntegerField()
        def __str__(self) -> str:
            return f'{self.student.student_name} {self.subject.subject_name}'

        # once a subject is added in a table, it should be unique
        class Meta:
            unique_together=['student','subject']

