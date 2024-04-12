from django.urls import path
from . import views

urlpatterns = [
    path('',views.Render_AboutPage,name='about')
]