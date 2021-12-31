## 12.05 현재 작성 중인 페이지
# 출처: https://github.com/nomadcoders/airbnb-clone/blob/a72e0f81fae79875d993cdb161b554f57e6fbd62/users/mixins.py
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    # 현재 작성 중
    login_url = reverse_lazy("users:login")

# 12.25 기존 코드를 바탕으로 임의로 작성 중인 view들
class DgistOnlyView():
    pass

class GistOnlyView():
    pass

class UnistOnlyView():
    pass

class PostechOnlyView():
    pass

class KaistOnlyView():
    pass