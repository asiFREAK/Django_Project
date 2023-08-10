from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.TextField(max_length=20)
    roll_no=models.IntegerField(primary_key=True)
    doa=models.DateField(auto_now_add=True)
    
class Clasroom(models.Model):
    class_name=models.TextField(max_length=10)
    class_teacher=models.TextField(max_length=20)
    
class Teachers(models.Model):
    name=models.TextField(max_length=20)
    qualification=models.TextField(max_length=20)
    id=models.IntegerField(primary_key=True)

class Marks(models.Model):
    DBMS=models.IntegerField(null=True,blank=True)
    DSA=models.IntegerField(null=True,blank=True)
    SE=models.IntegerField(null=True,blank=True)
    DCCN=models.IntegerField(null=True,blank=True) 
    LS=models.IntegerField(null=True,blank=True) 



#student name, roll no., dateofadmission