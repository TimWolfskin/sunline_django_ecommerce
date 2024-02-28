from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# from sunline import settings
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    path("user/", include("users.urls", namespace="user")),
    path("about/", include("about.urls", namespace="about")),
    path("contacts/", include("contacts.urls", namespace="contacts")),
    path("blog/", include("blog.urls", namespace="blog")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
