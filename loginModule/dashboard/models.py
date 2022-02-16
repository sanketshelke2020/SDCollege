from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import RelatedField
from django.core.mail import EmailMessage
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Course(models.Model):
    courseName = models.CharField(max_length=200)
    courseAbbr = models.CharField(max_length=10)
    courseImg = models.ImageField()

    def __str__(self):
        return f"${self.courseName} (${self.courseAbbr})"

class UserExtended(models.Model):
    user =models.OneToOneField(User, on_delete=CASCADE)
    course = models.ForeignKey(Course, on_delete=CASCADE, related_name= "courseusers" )

class Notice(models.Model):
    title = models.CharField(max_length=264)
    description = models.CharField(max_length=2048)
    date = models.DateField()
    file = models.FileField()
    course = models.ManyToManyField(Course, related_name="notice")


# email logic

@receiver(post_save,sender=Notice)
def sendEmail(sender, instance, **kwargs):
    emailArr = []
    for courses in instance.course.all():
        for uuser in courses.courseusers.all():
            emailArr.append(uuser.user.email)
            print(emailArr)
    
    noticeFile = instance.file

    email = EmailMessage("hello Registeration Successful","Kya huaa tera vada ", to = emailArr)
    email.attach(noticeFile.name, noticeFile.read())
    email.send()
