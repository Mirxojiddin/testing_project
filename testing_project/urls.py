
from django.contrib import admin
from django.urls import path, include

from testing_project.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('testing.urls')),
    path('users/', include('users.urls')),
    path('', IndexView.as_view(), name='index')

]
