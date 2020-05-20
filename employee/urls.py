from django.conf.urls import url

from employee import views

urlpatterns = [
    url('edit/',views.edit),
    url('delete/',views.delete),
    url('add/', views.add)
]