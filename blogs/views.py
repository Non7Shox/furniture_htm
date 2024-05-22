import self
from django.views.generic import ListView, DetailView

from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogsListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        blogs = BlogModel.objects.all()
        cat = self.request.GET.get('cat')
        if cat:
            blogs = blogs.filter(category=cat)

        context = {
            "blogs": blogs,
            "category": BlogCategoryModel.objects.all(),
            "tags": BlogTagModel.objects.all(),
            "famous_blogs": BlogModel.objects.all().order_by('created_at')[:2],
        }
        return context


class BlogDetailView(DetailView):
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'blog'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            "category": BlogCategoryModel.objects.all(),
            "blog": BlogModel.objects.get(pk=self.kwargs['pk']),
            "tags": BlogTagModel.objects.all(),
            "famous_blogs": BlogModel.objects.all().order_by('created_at')[:2],
            "related_blogs": BlogModel.objects.filter(category__in=self.object.category.all())[:3]
        }
        return context
