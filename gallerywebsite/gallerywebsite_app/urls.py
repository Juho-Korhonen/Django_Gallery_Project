from django.urls import path,include
from .views import display_gallerypage,display_specific_pic
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("<str:user_name>",display_gallerypage),
    path("<str:user_name>/<str:specific_pic>",display_specific_pic)

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)