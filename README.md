# lsqfit-dashboard

This repo is the start of an app which generates an interactive dashboard for nonlinear bayesian least-squares fitting of noisy data.

## Need

Fitting noisy data with multidimensional nonlinear functions is an important task in many (scientific) projects.
A versatile and well documented tool which has been employed in several publications is the python module [`lsqfit`](https://github.com/gplepage/lsqfit/tree/v11.5.1).
This project aims to simplify, streamline and thus speed up the process of running complicated fits.
In particular it aims to create a Graphical User Interfaces which allows to

* interact with parameters in an intuitive way to lower the barrier of entrance and speed up analysis
* compare fits for different models to make educated decisions about the best fit
* store fits to a database such previous work can be recovered and easily shared

## Dependencies

To make use of existing tools and speed up development, this software will be build in python and utilize existing modules.
The core components of the software will be

* [`lsqfit`](https://github.com/gplepage/lsqfit/tree/v11.5.1) for running the fits
* [Django](https://www.djangoproject.com) / [EspressoDB](https://github.com/callat-qcd/espressodb) for the multi-page application & data backend
* [Dash](https://plotly.com/dash/) for dynamically interacting with fits.

## State

Right now we are in the brain storming phase.
Features and layout is under construction and we are looking forward to receive input.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md)
