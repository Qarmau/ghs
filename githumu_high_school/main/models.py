from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
 
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News")

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

class About(models.Model):
    history = models.TextField(help_text="Enter each point on a new line")
    population = models.IntegerField()
    school_motto = models.CharField(max_length=200)
    vision = models.TextField()
    mission = models.TextField()
    subjects_offered = models.TextField(help_text="Enter each subject on a new line")
    clubs_and_societies = models.TextField(help_text="Enter each club/society on a new line")
    contact_information = models.TextField()
    email = models.EmailField()
    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("about")

class Administrator(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10,choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')])
    photo = models.ImageField(upload_to='admin_photos/')
    order = models.IntegerField(default=0)
    role = models.CharField(max_length=100, blank=True, choices=[('Chief Principal','Chief Principal'),('D/Admin','D/Admin'),('D/Acad','D/Acad'),('Dean','Dean'),('HOD','HOD'),('HOS','HOS')])
    subjects = models.CharField(max_length=200)

class TeachingStaff(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')])
    role = models.CharField(max_length=100, blank=True, choices=[('Chief Principal','Chief Principal'),('D/Admin','D/Admin'),('D/Acad','D/Acad'),('Dean','Dean'),('HOD','HOD'),('HOS','HOS')])
    subjects = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='staff_photos/')
    order = models.IntegerField(default=0)

class Achievement(models.Model):
    year = models.IntegerField()
    university_admission_rate = models.FloatField()

class CoCurricularAward(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='award_photos/')

class HolidayAssignment(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=50)
    file = models.FileField(upload_to='assignments/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Background Image {self.order}"
