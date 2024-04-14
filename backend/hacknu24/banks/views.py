from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .utils import jusanScrape
from .models import BankCard, CashbackOffer
from .serializers import BankCardSerializer, CashbackOfferSerializer

# jusanScrape()


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
        bank_card = get_object_or_404(queryset, pk=pk)
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


class CashbackOfferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CashbackOffer.objects.all()
    serializer_class = CashbackOfferSerializer

    def get_queryset(self):
        category = self.request.data.get('category')  # Access category from request data
        if category:
            return CashbackOffer.objects.filter(category=category)
        else:
            # Return all cashback offers if no category is provided
            return CashbackOffer.objects.all()
    
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        cashback_offer = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(cashback_offer)
        return Response(serializer.data)

