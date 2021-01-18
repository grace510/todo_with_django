
#프로젝트의 urls.py에 의해 호출됨

from django.urls import path, include
from . import views  #from . : 경로상 같은 위치

urlpatterns = [
    path('',views.index,name='index'), #아무 입력없을때의 home
    path('createTodo/',views.createTodo,name='createTodo'),#createTodo 요청에 대한 처리. (html action = ./createTodo)
    path('deleteTodo/',views.deleteTodo,name='deleteTodo'),#createTodo 요청에 대한 처리. (html action = ./createTodo)

]

#view.py의 어떤 메소드와 연결될 것인지