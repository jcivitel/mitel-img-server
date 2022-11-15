from django.urls import path
from . import views

urlpatterns = [
    path("<str:customer>/idlescreen_<str:phonemodel>.png", views.get_image)
]
