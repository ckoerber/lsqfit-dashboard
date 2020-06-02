"""Models of fits
"""

# Note: if you want your models to use espressodb features, they must inherit from Base

from django.db import models
from espressodb.base.models import Base
from django.urls import reverse_lazy

# from django_gvar.models import GVarField
from lsqfit_dashboard.fits.fields import SymbolField


class Data(Base):
    x = models.JSONField(null=False, blank=False, default=list)
    y = models.JSONField(null=False, blank=False, default=list)

    def get_absolute_url(self):
        return reverse_lazy("fits:data-detail", kwargs=dict(pk=self.pk))


class FitModel(Base):
    name = models.CharField(max_length=255, help_text="Name of the fit model")
    fit_function = SymbolField(null=False, blank=False)
    meta_parameters = models.JSONField(null=False, blank=True, default=dict)
    default_parameters = models.JSONField(null=False, blank=False, default=dict)

    def get_absolute_url(self):
        return reverse_lazy("fits:fit-model-detail", kwargs=dict(pk=self.pk))


class FitResult(Base):
    model = models.ForeignKey(FitModel, on_delete=models.CASCADE)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    prior = models.JSONField()
    posterior = models.JSONField()
