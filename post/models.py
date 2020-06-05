from django.db import models

# Create your models here.
class Post(models.Model):
        post_heading = models.CharField(max_length=200)
        post_text = models.TextField()

        def __str__(self):
            return self.post_heading

class Like(models.Model):
    post = models.ForeignKey(Post,null=True,on_delete=models.SET_NULL)
    likesum = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.post)