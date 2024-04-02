from django.core import serializers
from django.shortcuts import render
from .models import Topic, Subtopic, Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TopicForm, SubtopicForm, QuestionForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView

@login_required
class TopicList(LoginRequiredMixin, ListView): #Creates a topic list
    model = Topic
    context_object_name = 'topic'
    template_name = 'eduprod/topic_list.html'
    
class TopicCreate(LoginRequiredMixin, CreateView): #Allows the user to create a new topic
    model = Topic
    form_class = TopicForm
    template_name = 'eduprod/topic_form.html'
    success_url = reverse_lazy('eduprod:topic_list')  # Redirect to the topic list page after creating

class TopicDelete(LoginRequiredMixin, DeleteView): #Allows the user to delete a topic
    model = Topic
    template_name = 'eduprod/topic_confirm_delete.html'
    success_url = reverse_lazy('eduprod:topic_list')  # Redirect to the topic list page after deleting

class SubtopicCreate(LoginRequiredMixin, CreateView): #Allows the user to add a new subtopic
    model = Subtopic
    form_class = SubtopicForm
    template_name = 'eduprod/subtopic_form.html'
    success_url = reverse_lazy('eduprod:subtopic_list')  # Redirect to the subtopic list page after creating

class SubtopicUpdate(LoginRequiredMixin, UpdateView): #Allows the user to update a subtopic
    model = Subtopic
    form_class = SubtopicForm
    template_name = 'eduprod/subtopic_form.html'
    success_url = reverse_lazy('eduprod:subtopic_list')  # Redirect to the subtopic list page after updating


class SubtopicDelete(LoginRequiredMixin, DeleteView): #Allows the user to delete a subtopic
    model = Subtopic
    template_name = 'eduprod/subtopic_confirm_delete.html'
    success_url = reverse_lazy('eduprod:subtopic_list')  # Redirect to the subtopic list page after deleting

class SubtopicList(LoginRequiredMixin, ListView): #Creates a subtopic list
    model = Subtopic
    context_object_name = 'subtopic'
    template_name = 'eduprod/subtopic_list.html'

    def get_queryset(self):
        topic_id = self.kwargs['pk']
        return Subtopic.objects.filter(topic_name_id=topic_id)

class QuestionCreate(LoginRequiredMixin, CreateView): #Allows the user to add a questions
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after creating

class QuestionUpdate(LoginRequiredMixin, UpdateView): #Allows the user to update a question
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after updating

class QuestionDelete(LoginRequiredMixin, DeleteView): #Allows the user to delete a question
    model = Question
    template_name = 'eduprod/question_confirm_delete.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after deleting

class QuestionList(LoginRequiredMixin, ListView): #Creates a question list
    model = Question
    context_object_name = 'questions'
    template_name = 'eduprod/question_list.html'

    def get_queryset(self):
        subtopic_id = self.kwargs['pk']
        return Question.objects.filter(subtopic_name_id=subtopic_id)
