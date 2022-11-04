from django.urls import path , include
from rest_framework import routers 
from .api import ToDAPIViewSet
from .views import todo_list



router = routers.DefaultRouter()
router.register('todo', ToDAPIViewSet)

app_name = 'todo'

urlpatterns = [
    path('' , todo_list),
    path('api/' , include(router.urls)),
]
