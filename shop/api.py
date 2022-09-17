from rest_framework.viewsets import ModelViewSet
from shop.models import Category, Product
#from rest_framework.permissions import IsAuthenticated


from shop.serializers import CategorySerializer, ProductListSerializer,ProductdetailSerialiazer



class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    
    
    
    def get_queryset(self):
        return  Category.objects.all()
 
 
class ProductViewset(ModelViewSet):
    
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductdetailSerialiazer
    
    queryset = Product.objects.all()