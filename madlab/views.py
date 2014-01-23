from django.shortcuts import render, get_object_or_404
from madlab.models import Post
# Create your views here.
def index(request):
        # get the posts that are published
        posts = Post.objects.filter(published=True)
        # now return the rendered template
        return render(request, 'madlab/index.html', {'posts': posts})
     
def post(request, slug):
        # get the Post object
        post = get_object_or_404(Post, slug=slug)
        # now return the rendered template
        return render(request, 'madlab/post.html', {'post': post})
