from django.shortcuts import reverse, render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import News, Cat
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from .utils import DataMixin, menu_header
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsMain(DataMixin, ListView):
    model = News 
    template_name = 'news/index.html'
    context_object_name = 'post'
    title_page = 'Главная страница'
    
    def get_queryset(self):
        return News.published.all()



def about(request):
    data ={
        'title':"О сайте",
        'menu':menu_header,
    }
    return render(request, 'news/about.html', data)


class AddPost(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'news/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('main')
    title_page = 'Предложить новость'
    



    def form_valid(self, form):
        w = form.save(commit=False)  
        w.author = self.request.user
        w.save()  
        return super().form_valid(form)


def contact(request):
    data ={
        'title': 'Обратная связь',
        'menu': menu_header,
    }
    return render(request, 'news/contact.html', data)

def login(request):
    return HttpResponse('Авторизация')


class ShowPost(DataMixin, DetailView):
    template_name ='news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name ='post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(News.published, slug=self.kwargs[self.slug_url_kwarg])


class NewsCategory(DataMixin, ListView):
    template_name = 'news/index.html'
    context_object_name = 'post'


    def get_queryset(self):
        return News.published.filter(cat__slug=self.kwargs['cat_slug'])


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['post'][0].cat
        return self.get_mixin_context(context, title=cat.name)
        
        

    