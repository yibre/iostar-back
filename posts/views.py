from django.shortcuts import render
from . import models, forms
from bands.models import Band
from comments.models import Comment
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, UpdateView, FormView, View
from comments.forms import CommentForm
from django.urls import reverse_lazy
from django.db.models import Q

# Promotions

class PromotionListView(ListView):
    promotionBand = Band.objects.filter(name="promotions")
    queryset = promotionBand[0].posts.order_by('created')
    context_object_name = "posts"
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    template_name="posts/promotions/main.html"

def count_views(request, post_id):
    post_object = models.Post.objects.get(id=post_id)
    post_object.views = post_object.views +1
    post_object.save()


def post_delete(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.delete()
        messages.success(request, "post deleted")
        return redirect(reverse("core:home"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))

def ad_edit(post_id):
    pass


class AddPhotoView(FormView):
    model = models.Photo
    template_name = "posts/add_photo.html"
    # 아직 미완성


class PromotionDetailView(DetailView):
    """ Detail Definitions """
    model = models.Post
    template_name="posts/promotions/promotion_detail.html"

    # 이 하단부 코드는
    # https://dontrepeatyourself.org/post/django-blog-tutorial-part-4-posts-and-comments/
    # 현재 코멘트 업로드 안되는 상황, 물론 잘 보여지긴 함
    # 에서 가져옴

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        # slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(models.Post, pk=pk)
        # post = get_object_or_404(models.Post, pk=pk, slug=slug)
        #comments = post.comment_set.all()
        comments = post.comment_set.order_by('created')

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = models.Post.objects.filter(id=self.kwargs['pk'])[0]
        comment = post.comment_set.all()

        context['post'] = post
        context['comment'] = comment
        context['form'] = form

        if form.is_valid():
            print("form is valid")
            writer = self.request.user
            comment = form.cleaned_data['comment']

            comment = Comment.objects.create(
                comment=comment, post=post, writer = writer
            )
            form = CommentForm()
            context['form'] = form
        # 해당 줄 부분 수정이 있음
        return redirect(reverse("posts:promotion_detail", kwargs={"pk": post.pk}))


class NoticeDetailView(DetailView):
    """ Detail Definitions """
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

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)
            results = models.Post.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, "posts/promotions/search.html", context)
    return render(request, "posts/promotions/search.html")