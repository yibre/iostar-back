from django.shortcuts import render
from models import Post

# Create your views here.
def count_views(request, post_id):
    post_object = Post.objects.get(id=post_id)
    post_object.views = post_object.views +1
    post_object.save()