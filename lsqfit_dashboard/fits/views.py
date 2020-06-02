from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from lsqfit_dashboard.fits.models import Data
from lsqfit_dashboard.fits.models import FitModel


class DataCreateView(CreateView):
    model = Data
    fields = ["tag", "x", "y"]
    template_name = "data_form.html"


class DataDetailView(DetailView):

    model = Data
    template_name = "data_detail.html"


class FitModelCreateView(CreateView):
    model = FitModel
    fields = ["tag", "fit_function", "meta_parameters", "default_parameters"]
    template_name = "fit_model_form.html"


class FitModelDetailView(DetailView):

    model = FitModel
    template_name = "fit_model_detail.html"
