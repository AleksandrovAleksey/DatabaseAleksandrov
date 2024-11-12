from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, ManyToManyField, ForeignKey




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to="", blank=True, null=True)
    def __str__(self):
        return str(self.user)


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.tag


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField(max_length=1000)
    tags = ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class Answer(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text


