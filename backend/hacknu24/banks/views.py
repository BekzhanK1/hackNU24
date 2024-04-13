from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import BankCard
from .serializers import BankCardSerializer

class BankCardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer
    
    def get_queryset(self):
        user = self.request.user
        return BankCard.objects.filter(user=user)     
    

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        bank_card = get_object_or_404(queryset, pk = pk)
        serializer = self.serializer_class(bank_card)
        return Response(serializer.data)
    
    def create(self, request):
        user = request.user
        data = request.data
        data['user'] = user.pk
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        bank_card = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(bank_card)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
        
