from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.contrib import messages
from posts.models import Post
# Create your views here.

class UploadCommentView(FormView):
    """
    iostream form에 있던 내용 그대로 가져옴
    """
    form_class = forms.UploadCommentForm
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