## 12.05 현재 작성 중인 페이지
# 출처: https://github.com/nomadcoders/airbnb-clone/blob/a72e0f81fae79875d993cdb161b554f57e6fbd62/users/mixins.py
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
