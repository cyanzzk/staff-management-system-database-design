from django.conf.urls import url

from department import views

urlpatterns = [
    url('edit/',views.edit),
    url('delete/',views.delete),
    url('add/', views.add),
url('admin/', views.admin)
]