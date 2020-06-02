"""Prepares the usage of the lsqfit_dashboard module
"""
import os
from django import setup as _setup


def _init():
    """Initializes the django environment for lsqfit_dashboard
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lsqfit_dashboard.config.settings")
    _setup()

    if os.environ.get("ESPRESSODB_INIT_CHECKS", "0") == "1":
        from espressodb.management.checks import run_all_checks

        try:
            run_all_checks()
        except Exception as error:
            msg = "Failed to import EspressoDB project!\n\n"
            msg += str(error)
            msg += "\n\nYou are seeing this error because,"
            msg += " on initialization, EspressoDB runs cross-checks."
            msg += " If you want to disable this behavior, set the"
            msg += " environment variable `ESPRESSODB_INIT_CHECKS=0`."

            raise RuntimeError(msg)


_init()
