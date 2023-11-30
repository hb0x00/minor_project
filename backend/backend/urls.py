from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home),
    path("auth/", include("AppAuth.urls"), name=""),
    path('admin/', admin.site.urls),
    path('projects/', include("Project.urls")),
    path("sitemap/", views.sitemap),
    path("company_profile/", views.company_profile),
    path("get-hired/", views.get_hired),
    path("register-company", views.register_company)
]
