from django.contrib import admin
from django.urls import path, include

from highlycomposite import views as highly_composite_views
from guides import views as guide_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', highly_composite_views.Home.as_view(), name='home'),
    path('heartbeat/', highly_composite_views.heartbeat, name='heartbeat'),
    path('guides/<slug:slug>/', guide_views.GuideDetail.as_view(), name='guide-detail'),
]
