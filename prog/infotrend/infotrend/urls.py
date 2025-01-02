
from django.contrib import admin
from django.urls import path, include
from news import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('users/', include('users.urls', namespace='users')),
]


admin.site.index_title = 'Новости'





