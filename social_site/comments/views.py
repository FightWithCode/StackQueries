from django.shortcuts import render
from django.views.generic import CreateView
from . import models
from posts.models import Post
from django.core.urlresolvers import reverse_lazy


class CreateCommentView(CreateView):
    model = models.Comment
    fields = ('comment_body','post',)
    success_url = reverse_lazy('posts:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
