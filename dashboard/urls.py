from django.urls import path
from dashboard import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     path('', views.index, name='index'),
     path('notes', views.notes, name='notes'),
     path('homework', views.homework, name='homework'),
     path('books', views.books, name='books'),
     path('dictionary', views.dictionary, name='dictionary'),
     path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
     path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
     path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
     path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
     path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
     path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
     path('youtube', views.youtube, name='youtube'),
     path('todo', views.todo, name='todo'),
     path('wiki', views.wiki, name='wiki'),
     path('conversion', views.conversion, name='conversion'),
     path('logout', views.userlogout, name='logout'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('profile', views.profile, name='profile'),

     


] 