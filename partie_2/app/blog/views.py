from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.blog.models import Post,Media,Article,Comment
from app.blog.forms import CommentForm
# Create your views here.

class PostListView(ListView):
    queryset=Post.objects.order_by('-date_create')
    context_object_name = 'posts'
    template_name='index.html'


class PostMediaView(ListView):
    model=Media
    context_object_name = 'images'
    template_name= 'image.html'


def ArticleView(request,pk):
    form = CommentForm()
    post=Post.objects.get(pk=pk)
    articles=Article.objects.filter(post_pk=pk).filter(publish=True).order_by('order_list')
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data['author'],
                content=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments=Comment.objects.filter(post=post).filter(approuved=True).order_by('-created_on')


    context={
        'articles':articles,
        'post':post,
        'form':form,
        'comments':comments,

    }
    return render(request,'article.html',context)

def PostCategories(request,tag):
    post=Post.objects.filter(categories__name__contains=tag).order_by('-date_create')
    context={
        "posts":post,
        'categories':tag
    }
    return render(request,'categories.html',context)
