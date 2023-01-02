from django.urls import path
from.import views



urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name = "delete-note"),
    path('notes-detail/<int:pk>',views.NoteDetailView.as_view(),name = "notes-detail"),
    path('youtube',views.youtube,name="youtube"),
    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name = "update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name = "delete-todo"),
]

  




