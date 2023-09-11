from django.urls import path
from.views import ClientListView
from.views import ClientDetailView

from.views import ReviewsListView
from.views import ReviewDetailView

from.views import OrderListView
from.views import OrderDetailView

from.views import PaymentDetailView
from.views import PaymentListView


urlpatterns = [
    path("clients/", ClientListView.as_view(), name = "client_list_view"),
    path("clients/<int:id>/", ClientDetailView.as_view(), name = "client_detail_view"),

    path('reviews',ReviewsListView.as_view(),name="reviews_list_view"),
    path('reviews/<int:id>/',ReviewDetailView.as_view(),name="reviews_detail_view"),
    
    path('reviews',ReviewsListView.as_view(),name="reviews_list_view"),
    path('reviews/<int:id>/',ReviewDetailView.as_view(),name="reviews_detail_view"),

    path('orders',OrderListView.as_view(),name="orders_list_view"),
    path('orders/<int:id>/',OrderDetailView.as_view(),name="orders_detail_view"),
    
    path('payments',PaymentListView.as_view(),name="payment_list_view"),
    path('payments/<int:id>/',PaymentDetailView.as_view(),name="payments_detail_view")

]