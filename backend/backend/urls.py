from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home),
    path("auth/", include("AppAuth.urls"), name=""),
    path('admin/', admin.site.urls),
    path('projects/', include("Project.urls")),
    path("sitemap/", views.sitemap),
    path("company_profile/", views.company_profile),
    path("get-hired/", views.get_hired),
    path("get-hired/hire_handler", views.hire),
    path("register-company/", views.register_company),
    path("register-company/register/", views.register_handler),
    path("recruiter-dashboard", views.recruiter_dashboard),
    # path('temp', views.model_form_upload)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)