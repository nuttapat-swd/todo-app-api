from django.urls import path, include
from task import views

urlpatterns = [
    path('tasks/',views.TaskListView.as_view(),name='task-list'),
    path('tasks/<int:pk>/',views.TaskDetailView.as_view(),name='task-detail'),
    path('tags/',views.TagsView.as_view(),name='task-tags'),
    path('status/',views.StatusView.as_view(),name='task-status'),

]
