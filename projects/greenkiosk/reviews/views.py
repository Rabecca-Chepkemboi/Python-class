from django.shortcuts import render
from reviews.models import Reviews
from django.shortcuts import redirect
from .forms import UploadReviewsForm
from django.contrib import messages

# Create your views here.
def upload_reviews(request):
    form = None  

    if request.method == "POST":
        form = UploadReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reviews uploaded successfully!')
            return redirect('reviews_upload_view')
    else:
        form = UploadReviewsForm()
        return render(request, "reviews/reviews_upload.html", {"form": form})
    
