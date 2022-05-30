from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.contrib import messages
from posts.models import Post
from django.views.generic import FormView
from django.shortcuts import get_object_or_404
# Create your views here.

class UploadCommentView(FormView):
    """
    iostream form에 있던 내용 그대로 가져옴
    """
    form_class = forms.CommentForm
    template_name = "partials/comments.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        iostream = form.save()
        iostream.author = self.request.user
        iostream.save()
        form.save_m2m()
        messages.success(self.request, "Advertisement Uploads")
        return redirect("iostream:main")

def comment_delete(request, id):
    comment = get_object_or_404(models.Comment, pk=id)
    blog_id = comment.post.id
    comment.delete()
    return redirect('posts:promotion_detail', blog_id)