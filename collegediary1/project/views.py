from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse    #not used here..
from .models import Project
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#blog views

#class based views:-
class ProjectListView(ListView):       #ListView for posts
    model = Project
    template_name = 'project/home.html'        # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    paginate_by = 5

class UserProjectListView(ListView):       #ListView for posts
    model = Project
    template_name = 'project/user_projects.html'        # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_posted')

class ProjectDetailView(DetailView):
    model = Project

                    #cannot use @login_required here coz it is fn decorator
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title','content', 'github_link', 'tag']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #return redirect(request, 'blog/home.html')         #or use get_absolute-url method

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title','content','github_link', 'tag']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})
