#from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from mainapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('hello/', views.HelloView.as_view(), name='hello'),
    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
