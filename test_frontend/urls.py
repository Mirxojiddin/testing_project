from django.urls import path

from test_frontend.views import FrontendTestRunnerView 

app_name = 'test_frontend'
urlpatterns = [
        path('<int:id>', FrontendTestRunnerView.as_view(), name = 'test')

]