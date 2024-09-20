from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'  # Шаблон для отображения
    context_object_name = 'news'
    queryset = Post.objects.filter(type='NW')  # Фильтрация новостей


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'  # Шаблон для отдельной новости
    context_object_name = 'news_item'


