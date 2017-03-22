from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^courses/destroy/(?P<id>\d+)$', views.confirm),
    url(r'^remove_course/(?P<id>\d+)$', views.remove),
]
