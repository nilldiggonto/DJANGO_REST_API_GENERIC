from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Novel(models.Model):
    title           = models.CharField(max_length=120)
    author          = models.CharField(max_length=120)
    description     = models.TextField()
    publish_date    = models.DateField()


    def __str__(self):
        return self.title


class Review(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    review_author   = models.ForeignKey(User,on_delete=models.CASCADE)
    review          = models.TextField(blank=True,null=True)
    rating          = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    novel           = models.ForeignKey(Novel,on_delete= models.CASCADE,related_name='review')

    def __str__(self):
        return str(self.rating)
