from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, ManyToManyField, ForeignKey
from django.utils import timezone


class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.annotate(like_count=models.Count('likes')).order_by('-like_count')

    def new_questions(self):
        return self.order_by('-created_at')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Answer by {self.user} to {self.question.title}'


class QuestionLike(models.Model):
    question = models.ForeignKey(Question, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.question.title}'


class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f'{self.user.username} likes answer to {self.answer.for_question}'
