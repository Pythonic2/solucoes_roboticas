from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView,SobreView
urlpatterns = [
   
    path('',HomeView.as_view(),name='home'),
    path('sobre/',SobreView.as_view(),name='sobre'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

