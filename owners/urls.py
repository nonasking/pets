from django.urls import path

from owners.views import OwnersView, DogsView

app_name = "owners"

urlpatterns = [
    path('/owner/', OwnersView.as_view()),
    path('/dogs/', DogsView.as_view()),
]
