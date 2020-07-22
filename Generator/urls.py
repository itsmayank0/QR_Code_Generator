from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomeView,name='Home'),
    path('generate',views.generate_qr,name='generate'),
    #path('/generated',views.getQRdata,name='generated'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
