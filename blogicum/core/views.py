"""Core views for error handling."""
from django.shortcuts import render


def page_not_found(request, exception):
    """Render 404 page."""
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """Render 500 page."""
    return render(request, 'pages/500.html', status=500)


def csrf_failure(request, reason=''):
    """Render 403 CSRF failure page."""
    return render(request, 'pages/403csrf.html', status=403)
