from django.urls import path
from . import views


urlpatterns = [
    path('', views.Message_List.as_view(), name='comments'),
    path('comments/<int:pk>', views.Message_detail.as_view(), name='comments_detail'),
    path('comments/post', views.CreateView.as_view()),
]