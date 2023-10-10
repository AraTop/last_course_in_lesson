from django.urls import path
from costumbre import views
from costumbre.apps import CostumbreConfig

app_name = CostumbreConfig.name

urlpatterns = [
   path("", views.HabitsListView.as_view(), name='list_habits'),
   path("<int:pk>/", views.HabitsDetailView.as_view(), name='detail_habits'),
   path("create/", views.HabitsCreateView.as_view(), name='create_habits'),
   path("delete/<int:pk>/", views.HabitsDeleteView.as_view(), name='delete_habits'),
   path("update/<int:pk>/", views.HabitsUpdateView.as_view(), name='update_habits'),
   path('send_message/<int:user_id>/<int:chat_id>/', views.SendMessageView, name='send_message'),
]
