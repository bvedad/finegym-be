from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path(
        "registration/", include('dj_rest_auth.registration.urls')
    ),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
]
