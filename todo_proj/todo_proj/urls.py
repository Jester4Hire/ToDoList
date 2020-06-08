from django.contrib import admin
from django.urls import path
from todo_app import views
from todo_app.views import detail_view
from todo_app.views import delete_view

urlpatterns = [
   path('', views.index, name="todo"),
   path('<id>', detail_view),
   path('<id>/delete', delete_view),
   path('admin/', admin.site.urls),
]
