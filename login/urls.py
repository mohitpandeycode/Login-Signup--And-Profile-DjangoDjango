
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.loginPage),
    path('signup/', views.signupPage),
    path('home/', views.index),
    path('links/<slug:id>', views.addLinks),
    path('logout/', views.handleLogout),
    path('changePassword/', views.change_password),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
