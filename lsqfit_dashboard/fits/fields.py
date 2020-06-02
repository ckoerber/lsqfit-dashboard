"""
"""
from typing import Union, Optional

from django import forms
from django.db.models.fields import Field
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from sympy import Symbol


class SymbolFormField(forms.Textarea):
    """
    """


class SymbolField(Field):
    """Field which stores gvars as TextFields
    """

    description = _("GVar")

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value: Union[Symbol, None, str]) -> Symbol:
        """Deserialze object
        """
        if isinstance(value, Symbol):
            return value

        if value is None:
            return value

        return Symbol(value)

    def get_prep_value(self, value: Symbol) -> str:
        return str(value)

    def value_to_string(self, obj: Symbol) -> str:
        """Serialize object
        """
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    @staticmethod
    def from_db_value(value: str, expression, connection):  # pylint: disable=W0613
        """Inverse of get_prep_value(). Called when loaded from the db

        See https://stackoverflow.com/q/48008026
        """
        if value is None:
            return value
        return Symbol(value)

    def formfield(self, **kwargs):
        # Passing max_length to forms.CharField means that the value's length
        # will be validated twice. This is considered acceptable since we want
        # the value in the form field (to pass into widget for example).
        return super().formfield(
            **{
                "max_length": self.max_length,
                **({} if self.choices is not None else {"widget": SymbolFormField}),
                **kwargs,
            }
        )
