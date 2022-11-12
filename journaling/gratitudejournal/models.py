from django.db import models
from datetime import date
# Create your models here.

class GratitudeJournal(models.Model):

    review_your_day = (
        (5,'Very Good'),
        (4,'Good'),
        (3,'Normal'),
        (2,'Bad'),
        (1,'Very Bad'),
    )

    journal_entry  =  models.TextField(help_text="Enter your Today's Journal Entry" )
    positive_experience = models.TextField(help_text="Share 1 positve experience which you experienced in past 24 Hours",blank=True)
    rate_your_day  =  models.PositiveSmallIntegerField("How is your Day", choices=review_your_day, default=5)
    date_created  = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    images = models.CharField("Please Choose your images", max_length=200,blank=True,null=True)

    
    def __str__(self):
        return f'{self.journal_entry}'


# class LifeLogJournal(models.Model):
#     entry = models.TextField(blank=True,null=True)


 
# class Attachment(models.Model):
#     gratitude_attach_key    = models.ForeignKey(GratitudeJournal , on_delete = models.CASCADE, related_name = 'gratitude_attach' , blank = True , null = True)
#     grat_attach_img         = models.ImageField(upload_to='gratitude_upload/',blank=True)
#     lifelog_attach_key      = models.ForeignKey(LifeLogJournal, on_delete=models.CASCADE , related_name='life_log_attach',blank=True,null=True)
#     lifelog_attach_image    = models.ImageField(upload_to='life_log_upload/',blank=True)
    
#     def __str__(self):
#         return f"{Attachment}"
    











    
        
