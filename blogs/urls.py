from django.urls import path

from blogs.views import BlogsListView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    path('', BlogsListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]
