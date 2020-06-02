# pylint: disable=C0103
"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from lsqfit_dashboard.fits.views import DataCreateView, DataDetailView
from lsqfit_dashboard.fits.views import FitModelCreateView, FitModelDetailView


app_name = "fits"
urlpatterns = [
    path("data-create/", DataCreateView.as_view(), name="data-create"),
    path("data-detail/<int:pk>/", DataDetailView.as_view(), name="data-detail"),
    path("fit-model-create/", FitModelCreateView.as_view(), name="fit-model-create"),
    path(
        "fit-model-detail/<int:pk>/",
        FitModelDetailView.as_view(),
        name="fit-model-detail",
    ),
]
