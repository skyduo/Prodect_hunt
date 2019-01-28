from django.urls import path, include
from . import views


urlpatterns = [
    path('publish/', views.publish, name='Publish_page'),
]