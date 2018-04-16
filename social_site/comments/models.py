from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='comment_by')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
