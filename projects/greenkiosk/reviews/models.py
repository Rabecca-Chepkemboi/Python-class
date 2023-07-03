from django.db import models

# Create your models here.

class Reviews(models.Model):
   product_id =  models.AutoField(primary_key=True)   
   review_text =  models.TextField()   
   rating = models.FloatField() 
   reviewer_name = models.CharField(max_length = 50)
   date_added = models.DateTimeField()
   num_votes = models.IntegerField() 
