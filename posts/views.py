from django.shortcuts import render

def post_view(request, post_id):
    if request.method == "GET":
        post_info = Post.objects.get(pk=post_id)
        return render(request, 'posts/post.html', {'post_info': post_info})
