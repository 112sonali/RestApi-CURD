from django.urls import path
from.views import *

urlpatterns = [

    path("",userapi.as_view()),
    path("userview/",userview.as_view()),
    path("listapi/<int:pk>/",listapi.as_view()),
    path("delete/<int:pk>/",deletedata.as_view())

    
]


