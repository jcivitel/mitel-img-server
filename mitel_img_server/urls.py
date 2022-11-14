from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('img/', include("mitel_img_generator.urls")),
]
