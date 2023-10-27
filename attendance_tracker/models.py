from django.db import models

# Create your models here.

class Student(models.Model):
    """A student who is enrolled in the college."""
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        """Returns a string representation of the student's name (last name, first name)."""
        return self.lname + ", " + self.fname
    
class Instructor(models.Model):
    """An instructor who works in the college."""
    id = models.IntegerField(max_length=6, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        """Returns a string representation of the instructor's name (last name, first name)."""
        return self.lname + ", " + self.fname
    
class Course(models.Model):
    """A course that is offered at the college."""
    course_code = models.CharField(max_length=12)
    course_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE) # Deletes all courses an instructor teaches if they are deleted from db.

    def __str__(self):
        """Returns a string of the course code, name, and instructor."""
        return self.course_code, ", " + self.course_name + ", " + self.instructor
