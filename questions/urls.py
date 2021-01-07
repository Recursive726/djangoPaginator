from . import views
from django.urls import path,include,re_path

urlpatterns = [
  
    re_path(r'^home/([0-9]{0,2})?$', views.question_list,name='question_list'),

]
