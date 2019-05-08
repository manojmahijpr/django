from django.shortcuts import render

from django.http import JsonResponse

# rest_framework imports
from rest_framework import generics
from .serializers import BlogPostSerializer
from .models import BlogPost
# Create your views here.


def blog_list(request):
    context = {
        'title': 'unique Title',
        'description': 'some description as well'
    }
    return JsonResponse(context)

def Home(request):
    return render(request, 'blog/index.html', {})


class BlogPostListView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer