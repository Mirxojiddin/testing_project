
from django.contrib import admin
from django.urls import path, include

from testing_project.views import IndexView, NewView, NewPassword, NewPasswordGet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('testing.urls')),
    path('users/', include('users.urls')),
    path('', IndexView.as_view(), name='index'),
    path('new', NewView.as_view(), name='new'),
    path('newP', NewPassword.as_view(), name='newP'),
    path('newF', NewPasswordGet.as_view(), name='newF')

]
