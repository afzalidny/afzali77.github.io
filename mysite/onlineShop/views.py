from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Post
def post_list(request):
    object_list = Post.objects.filter(status='published')
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
      post = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
      post = paginator.page(2)
    except EmptyPage:
     # If page is out of range deliver last page of results
      post = paginator.page(paginator.num_pages)
    return render(request,
    'onlineShop/post/list.html',
    {'page': page,
    'posts': post})
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
     status='published',
     publish__year=year,
     publish__month=month,
     publish__day=day)
    post.visits=post.visits+1
    post.save()
    return render(request,
     'onlineShop/post/detail.html',
     {'posts': post})