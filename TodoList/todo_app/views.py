from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse

# Create your views here.
# Request 처리하는 MVC의 controller 역할
# Request로부터 parameter값 받아서 valid check
# Busisness method(service) 호출 또는 한 공간에 구현
# MVC의 view (template) 에서 참조할 데이터 저장
# view (template) 선택,렌더링,리턴

#todo_app/
def index(request): #home
    todos = Todo.objects.all()
    context = {"todos":todos}
    return render(request,'todo_app/index.html',context)

#todo_app/createTodo
def createTodo(request):
    todoContent = request.POST['todoContent']
    new_todo = Todo(content=todoContent) #model에 변수로 데이터 넘겨줌
    new_todo.save()
    return HttpResponseRedirect(reverse('index')) #응답받으면 자동으로 index로 이동

#todo_app/deleteTodo
def deleteTodo(request):
    delete_todo_id = request.GET['id']
    todo = Todo.objects.get(id=delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index')) #응답받으면 자동으로 index로 이동



