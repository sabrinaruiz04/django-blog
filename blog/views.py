from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def index(request):
    latest_posts = Post.objects.all()[:3]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": all_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

def authors(request):
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": all_authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "blog/author_detail.html", {"author": author})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {"tags": all_tags})

def tag_posts(request, tag):
    tag_obj = get_object_or_404(Tag, name=tag)
    post_list = tag_obj.post_set.all()
    return render(request, "blog/tag_post.html", {"tag": tag_obj, "posts": post_list})