from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="index"),
    path("index",views.index, name="index"),
    path("create", views.create, name="create"),
    path("detail/<str:id>", views.detail, name='detail'),
    path("edit/<str:id>", views.edit, name='edit'),
    path("update_data",views.update, name="update_data"),
    path("delete", views.delete, name="delete")
]

# ... your URL patterns ...

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
