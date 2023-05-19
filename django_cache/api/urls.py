from django.urls import include, path
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('set_jwt_token/',
         views.set_jwt_token, name='set_jwt_token'),
    path('get_user_id_from_jwt_token/',
         views.get_user_id_from_jwt_token,
         name='get_user_id_from_jwt_token'),
]
