from django.conf.urls import url
from appone import views

app_name = "appone"

urlpatterns = [
    url(r'^pics/$',views.pics, name = "pics"),
]
