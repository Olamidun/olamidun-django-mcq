from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='index'),
    # path('<int:pk>', views.question_details, name='details'),
    path('results/', views.result, name='results'),
    # path('<int:question_id>/vote', views.vote, name='vote')
]