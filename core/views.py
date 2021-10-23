import re
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from posts.models import Post, Twinkle
from bands.models import Band
from lists.models import FavBand

def resolve_home(request):
    """
    메인 페이지에 들어갈 내용들
    1) posters: 홍보 자료들
    2) notice: 공지 자료들
    3) twinkles: 트윙클 최신글들 (top 5개)
    4) timetables: 시간표
    5) schedules: 스케쥴(필요한 스케쥴들 정리)
    notice = 
    twinkles =
    """
    promotionBand = Band.objects.filter(name="promotions")
    promotions = promotionBand[0].posts.order_by('created')[:3][::-1]
    # 프로모션 포스트의 상위 3개를 가져옴
    notices = Band.objects.filter(name="iostarnotice")[0].posts.all()
    twinkles = Twinkle.objects.all()

    return render(request, "home.html", {
        "posters": promotions,
        "notices" : notices, 
        "twinkles": twinkles
    })

class HomeView(ListView):
    """main page view"""

    model = Band
    context_object_name ="bands"
    template_name = "home.html"
    """
    각 밴드에 대한 링크
    1. 메인에 홍보 게시판
    2.
    """
    def get_queryset(self):
        pass