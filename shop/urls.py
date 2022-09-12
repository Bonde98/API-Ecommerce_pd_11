from django.urls import path,include

from shop.api import CategoryViewset,ProductViewset

from .views import   index,ProductDetail,ProductList
   
from rest_framework import routers
   
   
router = routers.SimpleRouter()
router.register('category',CategoryViewset,basename='category')
router.register('product',ProductViewset,basename='product')

   
urlpatterns = [
    path("", index, name="home"),
   path("shop/", ProductList.as_view(), name="product-list"),

    path("shop/<slug:slug>/details/",ProductDetail.as_view(), name="product-details"),
    path("category/<slug:category>",ProductList.as_view(),name="category_pots_list") ,    

    path("shop/<slug:slug>/details/",
         ProductDetail.as_view(), name="product-details"),
    
    # Les API
    path('api/',include(router.urls)),

]