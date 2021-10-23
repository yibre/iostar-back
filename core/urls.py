from bands.models import Band
from django.urls import path
from core.views import resolve_home

app_name = "core"

urlpatterns = [
    path("", resolve_home, name="home"),
    
]
"""
TODO: url 생성 및 홈페이지 설정하기,
홈페이지 설정할땐 어떻게 해야하지?
한 뷰에 여러가지 models를 섞어서 쓸 수 있나?

홈페이지 배너 만드는걸 고려해봐야할듯, 바로 posts랑 연결지어둘순 없으니까.

1. 메인 홈페이지 디자인
2. 홈페이지에 들어갈 url 설정 및 배너 디자인
3. 

"""