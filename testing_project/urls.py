
from django.contrib import admin
from django.urls import path, include

from testing_project.views import IndexView, NewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('testing.urls')),
    path('front/', include('test_frontend.urls')),
    path('users/', include('users.urls')),
    path('', IndexView.as_view(), name='index'),
    path('new', NewView.as_view(), name='new'),

]
