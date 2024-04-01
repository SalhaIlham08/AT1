from django.urls import path
from .views import TopicCreate, TopicDelete, TopicList
from .views import SubtopicCreate, SubtopicUpdate, SubtopicDelete, SubtopicList
from .views import QuestionCreate, QuestionUpdate, QuestionDelete, QuestionList
from . import views

urlpatterns = [
    path('topics/', views.TopicList.as_view(), name='topic_list'),
    path('topic/add/', views.TopicCreate.as_view(), name='topic_form'),
    path('topic/<int:topic_pk>/delete/', views.TopicDelete.as_view(), name='topic_confirm_delete'),

    path('topic/<int:topic_pk>/subtopics/', views.SubtopicList.as_view(), name='subtopic_list'),
    path('topic/<int:topic_pk>/subtopics/add/', views.SubtopicCreate.as_view(), name='subtopic_form'),
    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/edit/', views.SubtopicUpdate.as_view(), name='subtopic_edit'),
    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/delete/', views.SubtopicDelete.as_view(), name='subtopic_confirm_delete'),

    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/questions/', views.QuestionList.as_view(), name='question_list'),
    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/questions/add/', views.QuestionCreate.as_view(), name='question_form'),
    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/questions/<int:question_pk>/edit/', views.QuestionUpdate.as_view(), name='question_edit'),
    path('topic/<int:topic_pk>/subtopics/<int:subtopic_pk>/questions/<int:question_pk>/delete/', views.QuestionDelete.as_view(), name='question_confirm_delete'),
]
