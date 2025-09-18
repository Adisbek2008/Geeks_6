from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from users.permissions import IsModerator
from common.validators import validate_age_for_product_creation

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        validate_age_for_product_creation(self.request.user)
        serializer.save(owner=self.request.user)
