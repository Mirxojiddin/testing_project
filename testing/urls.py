from django.urls import path

from testing.views import TestingSampleView, TestRunnerView, TestReview, TestView , GoodreadsTestSample

app_name = 'testing'
urlpatterns = [
		path('', TestingSampleView.as_view(), name='sample'),
		path('test_runner/<int:id>', TestRunnerView.as_view(), name='test-runner'),
		path('review/<str:test>', TestReview.as_view(), name='review'),
		path('<int:id>/view', TestView.as_view(), name='test-view'),
		path('goodreads', GoodreadsTestSample.as_view(), name='goog')
]

