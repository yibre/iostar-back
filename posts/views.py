from django.shortcuts import render
from . import models, forms
from bands.models import Band
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, UpdateView, FormView, View

# Promotions

class PromotionListView(ListView):
    promotionBand = Band.objects.filter(name="promotions")
    queryset = promotionBand[0].posts.order_by('created')
    context_object_name = "posts"
    template_name="posts/promotions/main.html"

def count_views(request, post_id):
    post_object = models.Post.objects.get(id=post_id)
    post_object.views = post_object.views +1
    post_object.save()

def ad_delete(post_id):
    pass

def ad_edit(post_id):
    pass


class PromotionDetailView(DetailView):
    """ Detail Definitions     """
    model = models.Post
    template_name="posts/promotions/promotion_detail.html"


class NoticeView(ListView):
    """ iostar notice """
    promotionBand = Band.objects.filter(name="promotions")
    queryset = promotionBand[0].posts.order_by('created')
    context_object_name = "posts"
    template_name="posts/promotions/masonry_list.html"


class UploadAdView(FormView):
    """ upload advertisements form """
    form_class = forms.UploadAdForm
    template_name = "posts/promotions/upload_promotions.html"
    # 내가 저장한 포스터가 promotion band에 저장되도록 만들어야함

    def form_valid(self, form):
        post = form.save()
        post.author = self.request.user
        band = Band.objects.get(name="promotions")
        post.band = band
        post.save()
        form.save_m2m()
        messages.success(self.request, "Advertisement Uploads")
        return redirect(reverse("posts:promotion_detail", kwargs={"pk": post.pk}))


class EditPostView(UpdateView):
    model = models.Post
    template_name = "posts/post_edit.html"
    fields = {
        "title",
        "contents",
        "file"
    }

    def get_object(self, querset=None):
        post = super().get_object(queryset=querset)
        if post.author.pk != self.request.user.pk:
            raise Http404()
        return post

class HobbyHome(ListView):
    HobbyBand = Band.objects.filter(name="promotions")
    queryset = HobbyBand[0].posts.order_by('created')
    context_object_name = "posts"
    template_name = "posts/hobbies/main.html" 

class SchoolLife(ListView):
    template_name = "post/hobbies/main.html"

class CareerHome(ListView):
    pass


class SearchView(View):
    """ SearchView Definition """
    pass