"""yunyanjin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from yunyanjin.settings import MEDIA_ROOT
from shop.views import ProductDetailViewset, ProductPhotoViewset, ProductItemViewset
from cart.views import CartViewset
from users.views import UserViewset
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()

# 配置shop中product的url
router.register(r'productdetail', ProductDetailViewset, base_name='productdetail')

# 配置shop中photo的url
router.register(r'productphoto', ProductPhotoViewset, base_name='productphoto')

# 配置shop中Item的url
router.register(r'productitem', ProductItemViewset, base_name='productitem')

# 配置cart url
router.register(r'cart', CartViewset, base_name='cart')

# 注册
router.register(r'user', UserViewset, base_name='user')


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf 文档 title自定义
    path('docs', include_docs_urls(title='Amir')),

    path('api-auth/', include('rest_framework.urls')),

    # router 的url
    re_path('', include(router.urls)),

    # token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('login/', obtain_jwt_token)

]
