from django.conf.urls import url, include

from user import views


urlpatterns = [
    url(r'^regist/', views.regist),
    url(r'^upload/', views.uploadPhoto),
]


