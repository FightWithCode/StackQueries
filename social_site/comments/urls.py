from django.conf.urls import url
from . import views


app_name='comments'
urlpatterns = [
    url(r"^add/(?P<pk>[-\w]+)/$", views.CreateCommentView.as_view(), name='comment_form'),
]
