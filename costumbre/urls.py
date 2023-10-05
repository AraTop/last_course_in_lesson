from django.urls import path
from costumbre import views

urlpatterns = [
   path("", views.HabitsListView.as_view()),
   path("<int:pk>/", views.HabitsDetailView.as_view()),
   path("create/", views.HabitsCreateView.as_view()),
   path("delete/<int:pk>/", views.HabitsDeleteView.as_view()),
   path("update/<int:pk>/", views.HabitsUpdateView.as_view()),
   path('send_message/', views.SendMessageView.as_view(), name='send_message'),
]     