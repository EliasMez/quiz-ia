from django.db import models
 
# Create your models here.
class QuizModel(models.Model):
    user_answer1 = models.CharField(max_length=200,blank=False,null=True)
    user_answer2 = models.CharField(max_length=200,blank=False,null=True)
    user_answer3 = models.CharField(max_length=200,blank=False,null=True)
    user_answer4 = models.CharField(max_length=200,blank=False,null=True)
    user_answer5 = models.CharField(max_length=200,blank=False,null=True)
    user_answer6 = models.CharField(max_length=200,blank=False,null=True)
    user_answer7 = models.CharField(max_length=200,blank=False,null=True)
    user_answer8 = models.CharField(max_length=200,blank=False,null=True)
    user_answer9 = models.CharField(max_length=200,blank=False,null=True)
    user_answer10 = models.CharField(max_length=200,blank=False,null=True)
    
    def __str__(self):
        return self.user_answer1