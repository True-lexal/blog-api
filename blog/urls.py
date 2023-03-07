
from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import routers
from rest_framework.routers import SimpleRouter, Route

#
# class MyRouter(SimpleRouter):
#     routers = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         ),
#     ]


# router = routers.SimpleRouter()
# router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/articlelist/', ArticleApiList.as_view()),
    path('api/v1/articlelist/<int:pk>', ArticleApiUpdate.as_view()),
    path('api/v1/articledelete/<int:pk>', ArticleApiDelete.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
