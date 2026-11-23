from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serailizers import *
from .permissions import IsAdminOrReadOnly
from .filters import DishFilter,OrderFilter
from .pagination import CustomPagination


class Category_View(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class Category_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class Dish_View(ListCreateAPIView):
    queryset = Dish.objects.all().order_by('id')
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilter


class Dish_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]


class Order_View(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all().order_by('id')
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user).order_by('id')
        return Order.objects.none()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class Order_Detail(RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()


class Order_Update(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAdminUser]