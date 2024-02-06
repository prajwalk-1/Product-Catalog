
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
 
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('accounts/', include('accounts.urls')),
    #path('pdf/', include('pdf_convert.urls')),
    #path('emailsender/', include('send_email.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



