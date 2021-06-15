from django.shortcuts import render

def post_view(request): #(request, post_id)
    if request.method == "GET":
        return render(request, "posts/post.html")
        #post_info = Post.objects.get(pk=post_id)
        #return render(request, 'posts/post.html', {'post_info': post_info})
