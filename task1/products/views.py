from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
import requests

class ProductListView(APIView):
    def get(self, request, categoryname):
        # Fetch and filter products based on query parameters
        n = int(request.query_params.get('n', 10))
        page = int(request.query_params.get('page', 1))
        sort_by = request.query_params.get('sort_by', 'price')
        order = request.query_params.get('order', 'asc')

        # Fetch product data from external APIs (mocked here for demonstration)
        products = self.fetch_products_from_api(categoryname)

        # Sort and paginate
        products = sorted(products, key=lambda x: x[sort_by], reverse=(order == 'desc'))
        start = (page - 1) * n
        end = start + n
        products = products[start:end]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def fetch_products_from_api(self, categoryname):
        # Mock external API response for demonstration
        # Replace this with actual API calls to e-commerce sites
        mock_data = [
            {"product_id": "1", "name": "Laptop 10", "company": "Company A", "category": categoryname,
             "price": 4101, "rating": 2.67, "discount": 37, "availability": "out-of-stock"},
            {"product_id": "2", "name": "Laptop 20", "company": "Company B", "category": categoryname,
             "price": 5000, "rating": 4.5, "discount": 25, "availability": "in-stock"},
            # Add more products as needed
        ]
        return [Product(**product) for product in mock_data]

class ProductDetailView(APIView):
    def get(self, request, categoryname, productid):
        # Fetch product details
        product = self.fetch_product_detail_from_api(categoryname, productid)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def fetch_product_detail_from_api(self, categoryname, productid):
        # Mock external API response for demonstration
        # Replace this with actual API calls to e-commerce sites
        mock_data = {
            "product_id": "1", "name": "Laptop 10", "company": "Company A", "category": categoryname,
            "price": 4101, "rating": 2.67, "discount": 37, "availability": "out-of-stock"
        }
        return Product(**mock_data) if mock_data["product_id"] == productid else None
