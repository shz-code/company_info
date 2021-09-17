from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from companies.views import landing
from django.contrib.auth.views import LoginView , LogoutView

admin.site.site_title = 'Company_Info'
admin.site.site_header = 'Welcome To Company_Info Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing , name='home'),
    path('login/', LoginView.as_view() , name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('companies/', include('companies.urls' , namespace='companies')),
]

urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
