from django.shortcuts import render
from . import models, forms
from django.views.generic import ListView, DetailView, View, UpdateView, FormView

# Create your views here.
def count_views(request, post_id):
    post_object = Post.objects.get(id=post_id)
    post_object.views = post_object.views +1
    post_object.save()


class UploadAdView(FormView):
    """ upload advertisements form """
    form_class = forms.UploadAdForm
    template_name = "posts/advertisements/upload_promotions.html"
    # 내가 저장한 포스터가 promotion band에 저장되도록 만들어야함

    def form_valid(self, form):
        post = form.save()
        post.save()
        messages.success(self.request, "Advertisement Uploads")
        return redirect(reverse("posts:ad_detail", kwargs={"ads_pk": post.pk}))