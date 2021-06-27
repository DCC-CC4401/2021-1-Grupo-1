from django.shortcuts import render
from django.views import View

from posts.models import Post, PostImage


class HomepageView(View):

    def get(self, request):
        queryset = Post.objects.order_by("-post_date")[:10]
        images = []
        for p in queryset:
            photo = PostImage.objects.filter(post_id=p.id).first()
            images.append(photo)
        zipped = zip(queryset, images)
        return render(request, "adoptapp/homepage.html", {'posts': zipped})


class ResultsView(View):

    def get(self, request):
        return render(request, "adoptapp/results.html")