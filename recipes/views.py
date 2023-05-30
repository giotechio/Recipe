from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Recipe
from .serializers import RecipeSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer




#
# class RecipeList(generics.ListCreateAPIView):
#
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#
# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
