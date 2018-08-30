from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('public.urls')),
    path('bible/', include('bible.urls')),
    path('login/', auth_views.login, name='login'),
    path('account/', include('userProfile.urls')),
    path('account/team/', include('team.urls')),
    path('account/team/challenge/', include('challenge.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
