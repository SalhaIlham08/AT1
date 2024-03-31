from django import forms
from .models import Topic, Subtopic, Question

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']

class SubtopicForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())

    class Meta:
        model = Subtopic
        fields = ['topic_name', 'subtopic_name']
        
class QuestionForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())
    subtopic = forms.ModelChoiceField(queryset=Subtopic.objects.all())

    class Meta:
        model = Question
        fields = ['topic_name', 'subtopic_name', 'question_text', 'answer_text']

