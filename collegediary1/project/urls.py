from django.urls import path,include
from .views import(ProjectListView,
                  ProjectDetailView,
                  ProjectCreateView,
                  ProjectUpdateView,
                  ProjectDeleteView,
                  UserProjectListView)
from . import views

urlpatterns = [
    #path('', views.home , name = 'blog-home'),
    path('',ProjectListView.as_view(), name = 'project-home'),
    path('user/<str:username>',UserProjectListView.as_view(), name = 'user-projects'),
    path('<int:pk>/',ProjectDetailView.as_view(), name = 'project-detail'),
    path('new/',ProjectCreateView.as_view(), name = 'project-create'),
    path('<int:pk>/update/',ProjectUpdateView.as_view(), name = 'project-update'),
    path('<int:pk>/delete/',ProjectDeleteView.as_view(), name = 'project-delete'),
]

#as_view() by default expects-
#app - model_viewtype.html
#blog-post_list.html
