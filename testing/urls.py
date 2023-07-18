from django.urls import path

from testing.views import TestingSampleView

urlpatterns = [
		path('', TestingSampleView.as_view(), name='sample')


]

