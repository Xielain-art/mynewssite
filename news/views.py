from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import NewsForm, ContactForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News


def test(requets):
    if requets.method == 'POST':
        form = ContactForm(requets.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'django.test666@gmail.com',
                             ['rotmir.klimov@mail.ru'], fail_silently=True)
            if mail:
                messages.success(requets, 'Письмо успешно отправлено')
                return redirect('test')
            else:
                messages.error(requets, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(requets, 'news/test.html', {'form': form})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#
#     return render(request, 'news/add_news.html', {'form': form})
