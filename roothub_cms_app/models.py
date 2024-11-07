from django.db import models

# Create your models here.
class Admin(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class Trainers(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class Courses(models.Model):
  id = models.AutoField(primary_key=True)
  course_name = models.CharField (max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
  objects = models.Manager()

class Students(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  profile_pic = models.FileField()
  address = models.TextField()
  course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class Attendance(models.Model):
  id = models.AutoField(primary_key=True)
  course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
  attendance_date = models.DateTimeField(auto_now_add=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class AttendanceReport(models.Model):
  id = models.AutoField(primary_key=True)
  student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
  attendance_id = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING)
  status = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class FeedBackStudent(models.Model):
  id = models.AutoField(primary_key=True)
  student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
  feedback = models.TextField()
  feedback_reply = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class FeedBackTrainer(models.Model):
  id = models.AutoField(primary_key=True)
  trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
  feedback = models.TextField()
  feedback_reply = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class NotificationStudent(models.Model):
  id = models.AutoField(primary_key=True)
  student_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()

class NotificationTrainer(models.Model):
  id = models.AutoField(primary_key=True)
  trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()
