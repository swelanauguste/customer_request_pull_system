from django.urls import path

from . import views

urlpatterns = [
    path("", views.CustomerRequestListView.as_view(), name="list"),
    path(
        "detail/<slug:slug>/", views.CustomerRequestDetailView.as_view(), name="detail"
    ),
    path("create/", views.CustomerRequestCreateView.as_view(), name="create"),
    path("pull/<slug:slug>/", views.CustomerRequestPullUpdateView.as_view(), name="pull"),
]
