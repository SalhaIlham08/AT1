from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Topic(models.Model):
    Topic_Choices =[
    ('General', 'General Knowledge'),
    ('Mathematics'),
    ('Science'),
    ('English'),
    ('Social Science'),
    ('Software Engineering'),
    ('Engineering Studies'),
    ('Languages'),
    ]
    topic_name = models.CharField(max_length=200, choices=Topic_Choices, default='General')

    def __str__(self):
        return self.topic_name

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics', default='General')
    subtopic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subtopic_name

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=2000, default='')
    answer_text = models.CharField(max_length=20000, default='')

    def __str__(self):
        return self.question_text
    