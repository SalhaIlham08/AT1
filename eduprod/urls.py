from django.urls import path
from .views import TopicCreate, TopicDelete, TopicList
from .views import SubtopicCreate, SubtopicUpdate, SubtopicDelete, SubtopicList
from .views import QuestionCreate, QuestionUpdate, QuestionDelete, QuestionList
from . import views

urlpatterns = [
    path('topics/', TopicList.as_view(), name='topic_list'),
    path('topic/add/', TopicCreate.as_view(), name='topic_add'),
    path('topic/<int:pk>/delete/', TopicDelete.as_view(), name='topic_delete'),

    path('subtopics/', SubtopicList.as_view(), name='subtopic_list'),
    path('subtopic/add/', SubtopicCreate.as_view(), name='subtopic_add'),
    path('subtopic/<int:pk>/edit/', SubtopicUpdate.as_view(), name='subtopic_edit'),
    path('subtopic/<int:pk>/delete/', SubtopicDelete.as_view(), name='subtopic_delete'),
    
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('question/add/', QuestionCreate.as_view(), name='question_add'),
    path('question/<int:pk>/edit/', QuestionUpdate.as_view(), name='question_edit'),
    path('question/<int:pk>/delete/', QuestionDelete.as_view(), name='question_delete'),

     path('', views.index, name='index'),
    
]

