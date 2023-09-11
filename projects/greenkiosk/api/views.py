from rest_framework.views import APIView
from client.models import Client
from .serializers import ClientSerializer

from rest_framework.response import Response
from rest_framework import status

from reviews.models import Reviews
from.serializers import ReviewSerializer

from.serializers import OrderSerializer
from order.models import Order

from.serializers import PaymentSerializer
from payment.models import Payment

from inventory.models import Product
from.serializers import InventorySerializer


class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ClientSerializer(data = request.data)    
        if serializer.is_valid():
            serializer.save
            return Response (serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            


class ClientDetailView(APIView):
    def get(self, request, id, format = None):
        client = Client.objects.get(id = id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


    def put(self, request, id, format = None):
        client = Client.objects.get(id = id)
        serializer = ClientSerializer(client, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format = None):
        client = Client.objects.get(id = id)
        client.delete()
        return Response("client deleted", status = status.HTTP_204_CONTENT)     
     


class ReviewsListView(APIView):
    def get(self,request):
       reviews=ReviewSerializer.objects.all() ###querried data
       serializer=CustomerSerializer(reviews,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class ReviewDetailView(APIView):
    def get(self,request,id,format=None):
        review=Review.objects.get(id=id)
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        review= Review.objects.get(id=id)
        serializer=ReviewSerializer(review,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         review=Review.objects.get(id=id)
         review.delete()

         return Response("review deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
class OrderListView(APIView):
    def get(self,request):
       orders=OrderSerializer.objects.all() ###querried data
       serializer=OrderSerializer(orders,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class OrderDetailView(APIView):
    def get(self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        order= Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         order=Order.objects.get(id=id)
         order.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
class PaymentListView(APIView):
    def get(self,request):
       payments=Payment.objects.all() ###querried data
       serializer=PaymentSerializer(payments,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=PaymentSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class PaymentDetailView(APIView):
    def get(self,request,id,format=None):
        payment=Payment.objects.get(id=id)
        serializer=OrderSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        payment= Payment.objects.get(id=id)
        serializer=OrderSerializer(payment,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         payment=Payment.objects.get(id=id)
         payment.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)  

class InventoryListView(APIView):
    def get(self,request):
       payments=Payment.objects.all() ###querried data
       serializer=PaymentSerializer(payments,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=PaymentSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class InventoryDetailView(APIView):
    def get(self,request,id,format=None):
        payment=Payment.objects.get(id=id)
        serializer=OrderSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        payment= Payment.objects.get(id=id)
        serializer=OrderSerializer(payment,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         payment=Payment.objects.get(id=id)
         payment.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)     