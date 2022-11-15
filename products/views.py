from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product, Comment, Category

from products.permissions import IsAuthorOrReadOnly, IsSupplier
from products.serializers import (
    ProductSerializer,
    CommentSerializer
)


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsSupplier]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supplier=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSupplier]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = "pk"


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



