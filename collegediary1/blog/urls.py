from django.urls import path,include
from .views import(PostListView,
                  PostDetailView,
                  PostCreateView,
                  PostUpdateView,
                  PostDeleteView,
                  UserPostListView)
from . import views

urlpatterns = [
    #path('', views.home , name = 'blog-home'),
    path('',PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>',UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about , name = 'blog-about'),


    path('firstyear/ec/',PostListView.as_view(), name = 'firstyear-ec'),
    path('firstyear/ei/',PostListView.as_view(), name = 'firstyear-ei'),
    path('firstyear/cs/',PostListView.as_view(), name = 'firstyear-cs'),
    path('firstyear/it/',PostListView.as_view(), name = 'firstyear-it'),
    path('firstyear/mech/',PostListView.as_view(), name = 'firstyear-mech'),
    path('firstyear/civil/',PostListView.as_view(), name = 'firstyear-civil'),
    path('firstyear/elec/',PostListView.as_view(), name = 'firstyear-elec'),
    path('firstyear/chem/',PostListView.as_view(), name = 'firstyear-chem'),

    

]

#as_view() by default expects-
#app - model_viewtype.html
#blog-post_list.html
