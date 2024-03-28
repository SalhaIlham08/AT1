from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'section', 'question_text', 'answer_text']