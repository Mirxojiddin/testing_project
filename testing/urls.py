from django.urls import path

from testing.views import TestingSampleView, TestRunnerView

app_name = 'testing'
urlpatterns = [
		path('', TestingSampleView.as_view(), name='sample'),
		path('test_runner/<int:id>', TestRunnerView.as_view(), name='test-runner'),

]

