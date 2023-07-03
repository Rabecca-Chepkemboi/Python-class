from django.contrib import admin
from.models import Reviews


# Register your models here.

class ReviewsAdmin (admin.ModelAdmin):
    list_display = ("product_id", "review_text", "rating", "reviewer_name", "date_added", "num_votes")

admin.site.register(Reviews, ReviewsAdmin) 
