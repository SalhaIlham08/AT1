from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Topic(models.Model):
    TOPIC_CHOICES = [
        ('General', 'General Knowledge'),
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('Social Science', 'Social Science'),
        ('Software Engineering', 'Software Engineering'),
        ('Engineering Studies', 'Engineering Studies'),
        ('Languages', 'Languages'),
    ]
    topic_name = models.CharField(max_length=200, choices=TOPIC_CHOICES, default='General')

    def __str__(self):
        return self.get_topic_name_display()
    
class Subtopic(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics', default='Introduction')
    subtopic_name = models.CharField(max_length=200, default='General')

    def __str__(self):
        return self.subtopic_name

class Question(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic_name = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=2000, default='')
    answer_text = models.CharField(max_length=20000, default='')

    def __str__(self):
        return self.question_text
    