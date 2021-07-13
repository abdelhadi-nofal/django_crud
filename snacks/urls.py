from django.urls import path
from .views import SnackDeleteView, SnackListView,SnackDetailView,SnackCreateView, SnackUpdateView

urlpatterns = [

    path('',SnackListView.as_view(),name='snack'),
    path('<int:pk>',SnackDetailView.as_view(),name='snackdetail'),
    path('create',SnackCreateView.as_view(),name= 'snackcreate'),
    path('<int:pk>/update',SnackUpdateView.as_view(),name='snackupdate'),
    path('<int:pk>/delete',SnackDeleteView.as_view(),name='snackdelete')
]
