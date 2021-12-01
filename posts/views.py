from django.shortcuts import render
from . import models, forms
from bands.models import Band
from django.views.generic import ListView, DetailView, View, UpdateView, FormView

# Promotions

class PromotionListView(ListView):
    promotionBand = Band.objects.filter(name="promotions")
    queryset = promotionBand[0].posts.order_by('created')
    context_object_name = "posts"
    template_name="posts/advertisements/main.html"


def count_views(request, post_id):
    post_object = models.Post.objects.get(id=post_id)
    post_object.views = post_object.views +1
    post_object.save()

def ad_delete(post_id):
    pass

def ad_edit(post_id):
    pass


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


class PromotionDetail(DetailView):
    pass

class HobbyHome(ListView):
    pass

class SchoolLife(ListView):
    pass

class CareerHome(ListView):
    pass