
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import LinkList, LinkCreate, LinkDetail, CommentList
from django.views.generic import RedirectView


urlpatterns = patterns("",
    url("^$",
        LinkList.as_view(),
        name="home"),
    url("^yeniler/$",
        LinkList.as_view(), {"by_score": False},
        name="link_list_latest"),
    url("^best/$",
        LinkList.as_view(), {"by_score": True},
        name="link_list_best"),
    url("^link/create/$",
        login_required(LinkCreate.as_view()),
        name="link_create"),
    url("^link/(?P<slug>.*)/$",
        LinkDetail.as_view(),
        name="link_detail"),
    url("^users/(?P<username>.*)/links/$",
        LinkList.as_view(), {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/links/$",
        LinkList.as_view(), {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/comments/$",
        CommentList.as_view(), {"by_score": False},
        name="comment_list_user"),
#    url("^accounts/profile/$", RedirectView.as_view(url='/account/update')),
)
