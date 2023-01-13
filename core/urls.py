from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView
urlpatterns = [
   
    path('',HomeView.as_view(),name='home')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

