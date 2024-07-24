from django.urls import path
from django.contrib import admin
from main.views import index, blog, posting, new_post

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹의 첫 화면은 index 페이지 + URL 이름은 index
    path('', index),
    # URL/blog에 접속하면 blog 페이지 + URL 이름은 blog
    path('blog/', blog),
    path('blog/<int:pk>', posting, name="posting"),
    path('blog/new_post/', new_post),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)