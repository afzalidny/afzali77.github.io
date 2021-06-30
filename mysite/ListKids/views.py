from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import  Post_Kids,Comment
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

def post_kids_list(request, tag_slug=None):
    object_list = Post_Kids.objects.filter(status='published')
    tag = None
    if tag_slug:
      tag = get_object_or_404(Tag, slug=tag_slug)
      object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 2) # 3 posts in each page
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
    'ListKids/post/lists.html',
    {'page': page,   
    'posts': post,
    'tag': tag})
def post_kids_detail(request, year, month, day, post):
    post = get_object_or_404( Post_Kids,
     slug=post,
     status='published',
     publish__year=year,
     publish__month=month,
     publish__day=day)
   
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
    # A comment was posted
     comment_form = CommentForm(data=request.POST)
     if comment_form.is_valid():
    # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
    # Assign the current post to the comment
      new_comment.post = post
    # Save the comment to the database
      new_comment.save()
    else:
      comment_form = CommentForm()
    post.visits=post.visits+1
    post.save()
    # List of similar posts
    post_tags_ids =Post_Kids.tags.values_list('id', flat=True)
    similar_posts =Post_Kids.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request,
     'ListKids/post/details.html',
     {'posts': post,
     'comments': comments,
     'new_comment': new_comment,
     'comment_form': comment_form,
     'similar_posts': similar_posts
     })
def post_share(request, post_id):
 # Retrieve post by id
 post= get_object_or_404(Post_Kids, id=post_id, status='published')
 sent = False
 if request.method == 'POST':
 # Form was submitted
   form = EmailPostForm(request.POST)
   if form.is_valid():
      # Form fields passed validation
      cd = form.cleaned_data
      # ... send email
      post_url = request.build_absolute_uri(post.get_absolute_url())
      subject = f"{cd['name']} recommends you read "f"{post.title}"
      message = f"Read {post.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['subject']}"
      send_mail(subject, message, 'admin@myblog.com',
                [cd['to']])
      sent = True
 else:
    form = EmailPostForm() 
 return render(request, 
   'ListKids/post/share.html', {'posts': post,
   'form': form,
   'sent': sent})