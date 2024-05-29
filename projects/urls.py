from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# URL patterns for the Django project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # Include main_app URLs
    path('', include('main_app.urls')),
    # Include aboutus URLs
    path('', include('aboutus.urls')),
    # Include budgets URLs
    path('budgets/', include('budgets.urls')),
    # Include project_manager URLs
    path('project_manager/', include('pm.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
