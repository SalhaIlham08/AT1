from django import forms
from .models import Topic, Subtopic, Question

#Creates a form to input topic names
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']

#Creates a form to input subtopic names
class SubtopicForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())

    class Meta:
        model = Subtopic
        fields = ['topic_name', 'subtopic_name']

#Creates a form to input questions       
class QuestionForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())
    subtopic = forms.ModelChoiceField(queryset=Subtopic.objects.all())

    class Meta:
        model = Question
        fields = ['topic_name', 'subtopic_name', 'question_text', 'answer_text']

