from django.forms.models import modelformset_factory
from django.shortcuts import render
from . import models, forms
from bands.models import Band
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from users import mixins as user_mixins
from django.views.generic import View, ListView, DetailView, UpdateView, FormView
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect


class SchoolListView(ListView):
    """school 관련된 전체 게시글 list를 볼 수 있음 """
    model = models.SchoolPost
    template_name = "schoolposts/home.html"

class UploadSchoolPost(FormView):
    """
    school post들의 업로드를 위한 게시판, 기본적인 동작은 Post > UploadView와 동일하나 band 부분이 조금 달라짐
    """
    form_class = forms.UploadPostForm
    template_name = "posts/promotions/upload_promotions.html"

    def get_context_data(self, **kwargs):
        context = super(UploadSchoolPost, self).get_context_data(**kwargs)
        band_title = self.kwargs['band_title']
        school = self.kwargs['school_name']
        return context

    def form_valid(self, form):
        schoolpost = form.save()
        schoolpost.author = self.request.user
        band = self.kwargs['band_title']
        school = self.kwargs['school_name']
        try:
            band = Band.objects.get(name=band)
            post.band = band
            post.save()
            form.save_m2m()
            messages.success(self.request, "Advertisement Uploads")
            return redirect(reverse("posts:post_detail", kwargs={"band_title":band, "school_name": school_name, "pk": post.pk}))
        except:
            return redirect('https://iostar.site/404')


class EditPostView(FormView):
    """ post edit 가능함 """
    pass

class PostDetailView(DetailView):
    model = models.SchoolPost
    template_name="posts/promotions/promotion_detail.html"

    # 이 하단부 코드는
    # https://dontrepeatyourself.org/post/django-blog-tutorial-part-4-posts-and-comments/
    # 현재 코멘트 업로드 안되는 상황, 물론 잘 보여지긴 함
    # 에서 가져옴

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        band_title = self.kwargs["band_title"]
        post_title = self.kwargs["b"]
        band = get_object_or_404(Band, name=band_title)
        # BUG 1: 이 부분에 버그 있음. 가령 testband에 작성된 44번째 글 대신 promotions/44를 입력할 시 그대로 가게 됨
        pk = self.kwargs["pk"]
        form = CommentForm()
        post = get_object_or_404(models.Post, pk=pk)
        """
        하단은 BUG 1 이 수정되지 않은 코드임
        if post.band.name == band_title:
            return redirect('https://iostar.site/404')
        """
        comments = post.comment_set.order_by('created')
        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        band_title= self.kwargs["band_title"]
        school = self.kwargs['school_name']
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
        return redirect(reverse("posts:post_detail", kwargs={"band_title":band_title, "school_name": school_name, "pk": post.pk}))


# 하나의 post에 여러 photo를 업로드하는 방법

def school_verified_required(request):
    return render(request, "schoolposts/login_required.html")