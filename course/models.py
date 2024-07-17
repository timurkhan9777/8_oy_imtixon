from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video = models.FileField(upload_to="media/", validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'WMV'])
    ])
    created = models.DateTimeField(auto_now_add=True)


class LessonComment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class LikeLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson.title
