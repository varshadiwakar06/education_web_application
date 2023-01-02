from django.shortcuts import redirect, render
from.forms import*
from.models import *
from django.contrib import messages
from django.views import generic
from django.views.generic import DetailView
from youtubesearchpython import VideosSearch
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

@login_required
def notes(request):
    if request.method =="POST":
        form = NotesForm(request.POST)
        if form.is_valid():
             notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
             notes.save()
        messages.success(request,"Notes added successfully")
    else:
        form = NotesForm()
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

@login_required
def delete_note(request,pk = None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes") 


class NoteDetailView(generic.DetailView):
    model = Notes


def youtube(request):
    if request.method =="POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+= j['text']
            result_dict['description']= desc
            result_list.append(result_dict)
            context = {
                'form' : form,
                'results': result_list
            }
        return render(request,'dashboard/youtube.html',context)
    else:
            form = DashboardForm()
    context = {"form":form}
    return render(request,"dashboard/youtube.html",context)

@login_required
def todo(request):
     if request.method == 'POST':
        form = TodoForm(request.Post)
        if form.is_valid():
            try:
                finshed = request.POST["is_finished"]
                if finished == 'on':
                    finished = True
                else:
                    finished = False    
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request,f"Todo Added from {request.user.username}!")
        else:
            form = TodoForm()
            todo = Todo.objects.filter(user=request.user)
            if len(todo) == 0:
                todos_done = True
            else:
                todos_done = False
            context = {
            'form' : form,
            'todos' : todo,
            'todos_done' : todos_done
    }
        return render(request,"dashboard/todo.html",context)


@login_required
def update_todo(request,pk = None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished== True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

@login_required
def delete_todo(request,pk = None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created successfully of {username}!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request,"dashboard/register.html",context)
#varsha_diwakar
#admin@123
#3:58 

@login_required
def profile(request):
    todos = Todo.objects.filter(is_finished = False,user=request.user)
    if len(todos) ==0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'todos' : todos,
        'todos_done' : todos_done

    }
    return render(request,"dashboard/profile.html",context)