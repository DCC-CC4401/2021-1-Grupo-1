from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from posts.models import Post, PostImage


class HomepageView(View):

    def get(self, request):
        return render(request, "adoptapp/homepage.html")


def results_view(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(description__icontains=query)
    images = []
    for p in results:
        photo = PostImage.objects.filter(post_id=p.id).first()
        images.append(photo)
    results = list(zip(results, images))
    paginator = Paginator(results, 3)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)
    return render(request, "adoptapp/results.html", {'results': page_obj})


class ResultsView(View):

    def get(self, request):
        return render(request, "adoptapp/results.html")