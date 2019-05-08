from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.contrib import messages

from .forms import PostModelForm

from .models import PostModel
# Create your views here.





# def post_model_create_view(request):

#     if request.metod == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid:
#             form.save(commit=false)
#             print(form.cleaned_data)

#     form = PostModelForm()
#     context = {
#         'form': form
#     }
#     template = 'blog/create-view.html'
#     return render(request, template, context)


def post_model_update_view(request, id=None):

    data = get_object_or_404(PostModel, id=id)

    form = PostModelForm(request.POST or None, instance=data)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Updated post!')
        return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))

    context = {
        'form': form,
    }
    template = 'blog/update-view.html'
    return render(request, template, context)



def post_model_create_view(request):

    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(form.cleaned_data)
        obj.save()
        messages.success(request, 'Created a new blog post!')
        form = PostModelForm()
        # return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))

    context = {
        'form': form
    }
    template = 'blog/create-view.html'
    return render(request, template, context)


# @login_required( login_url='/login' )
# @login_required
# def post_model_list_view(request):
#     # print(qs)
#     print(request.user.is_authenticated)
#     if request.user.is_authenticated:
#         template = 'blog/list-view.html'
#     else:
#         template = 'blog/list-view-public.html'
#         raise Http404

#     qs = PostModel.objects.all()

#     context = {
#         'posts': qs
#     }
#     return render(request, template, context)
#     #return HttpResponse('some data')

# def post_model_list_view(request):
#     # print(qs)
#     print(request.user.is_authenticated)
#     if request.user.is_authenticated:
#         template = 'blog/list-view.html'
#     else:
#         template = 'blog/list-view-public.html'
#         return HttpResponseRedirect('/login/')

#     qs = PostModel.objects.all()

#     context = {
#         'posts': qs
#     }
#     return render(request, template, context)
#     #return HttpResponse('some data')


def post_model_list_view(request):
    
    query = request.GET.get('q')
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query)
            )
    
    context = {
        'posts': qs
    }
    template = 'blog/list-view.html'
    return render(request, template, context)
    #return HttpResponse('some data')


def post_model_detail_view(request, id=None):
    
    print(id)
    # Way one
    # try:
    #     post = PostModel.objects.get(id=100)
    # except:
    #     raise Http404

    # Way two
    # qs = PostModel.objects.filter(id=100)
    # if not qs.exists() and qs.count() != 1:
    #     raise Http404
    # else:
    #     post = qs.first()


    # post = PostModel.objects.get(id=1)
    post = get_object_or_404(PostModel, id=id)
    context = {
        'post': post,
    }
    template = 'blog/detail-view.html'
    return render(request, template, context)



def post_model_delete_view(request, id=None):
    
    post = get_object_or_404(PostModel, id=id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post Deleted!')
        return HttpResponseRedirect('/blog/list')
    context = {
        'post': post,
    }
    template = 'blog/delete-view.html'
    return render(request, template, context)


def post_model_search_view(request):
    query = request.GET.get('q')
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(title__icontains=query)
    context = {
        'posts' : qs
    }
    template = 'blog/list-view.html'
    return render(request, template, context)