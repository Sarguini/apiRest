from django.urls import path
from django.urls.resolvers import URLPattern
from serializator import views


urlpatterns = [
    path('serializator/', views.meteor_list),
    path('serializator/<int:pk>/', views.meteor_detail),
]
