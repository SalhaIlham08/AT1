from django import forms
from .models import Topic, Subtopic, Question

class TopicForm(forms.ModelForm):
    class Meta:
        topic = forms.ModelChoiceField(queryset=Topic.objects.all())
        model = Topic
        fields = ['name']

class SubtopicForm(forms.ModelForm):
    class Meta:
        model = Subtopic
        fields = ['topic', 'name']
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'subtopic', 'question_text', 'answer_text']
