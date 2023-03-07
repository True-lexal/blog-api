from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import *
from .permissions import *
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleApiList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


class ArticleApiUpdate(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ArticleApiDelete(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class ArticleViewSet(ModelViewSet):
#     # queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Article.objects.all()[:3]
#         else:
#             return Article.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cat = Category.objects.get(pk=pk)
#         return Response({'cats': cat.name})


# class ArticleApiView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleApiUpdate(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleApiDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleApiView(APIView):
#     def get(self, request):
#         w = Article.objects.all()
#         return Response({'all': ArticleSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'result': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'No right request'})
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Record is not exist'})
#         serializer = ArticleSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({'change': serializer.data})
#
#     def delete(self, request, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'No such record'})
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Record is not exist'})
#         instance.delete()
#         return Response({'ok': f'{pk} deleted'})
#
#
# class ArticleApiView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
